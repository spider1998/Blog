# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import ArticleColumn
from django.contrib import admin

# Register your models here.
class ArticleColumnAdmin(admin.ModelAdmin):
    list_display = ("column","create","user")
    list_filter = ("column",)

admin.site.register(ArticleColumn,ArticleColumnAdmin)
