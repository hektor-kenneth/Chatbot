# -*- coding: utf-8 -*-
"""
Created on Fri Aug 04 23:32:58 2017

@author: Kenneth
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]