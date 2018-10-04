#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: jian
@file: forms.py
@time: 2018/10/4 12:07
"""
from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
