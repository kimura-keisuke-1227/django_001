#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 00:40:07 2021

@author: owner
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('next', views.next, name='next'),
    ]
