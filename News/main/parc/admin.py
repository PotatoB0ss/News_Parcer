from django.contrib import admin
from .models import News


@admin.register(News)
class News_Mod(admin.ModelAdmin):
    list_display = ('title', 'time', 'categ')
    list_display_links = ('title',)
    search_fields = ('title', 'time',)

    change_form_template = 'parc/parcing.html'



