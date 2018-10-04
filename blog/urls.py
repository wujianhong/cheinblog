#!/usr/bin/env python
# conding: uft-8
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('upload', views.upload),
]
