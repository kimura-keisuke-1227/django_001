#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 00:40:07 2021

@author: owner
"""

from django.conf.urls import url
from .views import HelloView

urlpatterns = [
        url('',HelloView.as_view(),name="index"),
    ]
