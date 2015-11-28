# -*- coding:utf-8 -*-
from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
   
    list_display = ('title', 'text', 'publish_date')
    ordering = ('title',)
     
admin.site.register(News, NewsAdmin)    
