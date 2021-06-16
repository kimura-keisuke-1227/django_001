#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 09:05:55 2021

@author: owner
"""

from django import forms

class HelloForm(forms.Form):
    id = forms.IntegerField(label='ID')
    #check = forms.BooleanField(label="CheckBox" , required=False)
    #
    name = forms.CharField(label='name')
    mail = forms.CharField(label='mail')
    gender = forms.BooleanField(label='gender',required=False)
    age = forms.IntegerField(label='age')
    birthday = forms.DateTimeField(label='birth')