import requests
from bs4 import BeautifulSoup
from datetime import date
import sqlite3


today = date.today()


def scrap():
# Проверка нет ли записей уже в базе данных по заголовку и ток потом добавление
# Всего проверяет 100 последних записей
    conn = sqlite3.connect('C:\Pycharm Projects\\News\main\db.sqlite3', check_same_thread=False)

    def check(dannie):
        c = 0
        count = 0

        sqll = "SELECT title FROM parc_news ORDER BY -time LIMIT 100"
        zapr = "SELECT id FROM parc_news ORDER BY id DESC LIMIT 1"
        cursor = conn.cursor()
        curs = conn.cursor()
        a = curs.execute(zapr)
        res = cursor.execute(sqll)

        for els in a:
            for lol in els:
                c = int(lol) + 1

        for elems in res:
            if dannie['title'] in elems:
                count += 1
                break

        if count == 0:
            try:
                sql = f"INSERT INTO parc_news VALUES ({c},'{dannie['title']}','{dannie['content']}','{dannie['time']}','{dannie['span']}');"
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
            except:
                pass

    #Сам парсер || Пока что много информации мне не нужно, так что парсит только первую страницу (18 записей)
    def pars():
        base_url = "https://lenta.ru"
        url = "https://lenta.ru/parts/news"
        resp = requests.get(url)
        html = resp.text
        soup = BeautifulSoup(html, 'html.parser')

        block = soup.select_one("div.parts-page__wrap")
        prod = block.find_all("li")

        for ele in prod:
            data = {}
            title = ele.select_one("h3.card-full-news__title")
            try:
                data['title'] = title.text
            except:
                continue

            try:
                span = ele.find("span").text
                data['span'] = span

                time = ele.find("time").text
                data['time'] = str(today) + " " + time
            except:
                continue

            new_url = ele.select_one("a")['href']
            if "http" in new_url:
                new_url = new_url
            if "http" not in new_url:
                new_url = base_url + new_url

            #New Page
            new_resp = requests.get(new_url)
            new_html = new_resp.text
            new_soup = BeautifulSoup(new_html, 'html.parser')

            try:
                content = new_soup.select_one('div.topic-body._news')
                rrr = content.find_all('p')
                otdam = ''
                for ele in rrr:
                    otdam += ele.text + "\n"

                data['content'] = otdam
            except:
                continue

            if data['content'] != None:
                check(data)

    pars()
    conn.close()






