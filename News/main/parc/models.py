from django.db import models


class News(models.Model):
    title = models.TextField(verbose_name="Заголовок новости")
    content = models.TextField(verbose_name="Содержимое новости")
    time = models.CharField(max_length=25, verbose_name="Дата и Время")
    categ = models.CharField(max_length=30, verbose_name="Категория", null=True)


    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.title