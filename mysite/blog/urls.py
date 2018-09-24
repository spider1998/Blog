# !/usr/bin/python
# -*- encoding: utf-8 -*-
# @author:spider1998
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.blog_title,name="blog_title"),
    url(r'(?P<article_id>\d)/$',views.blog_article,name="blog_detail"),
]