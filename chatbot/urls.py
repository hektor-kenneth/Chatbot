# -*- coding: utf-8 -*-
"""
Created on Fri Aug 04 23:32:58 2017

@author: Kenneth
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin

from slack_webhook import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^webhook', views.webhook, name='webhook'),
]