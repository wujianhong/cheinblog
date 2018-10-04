# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length=255)
    chinese_name = models.CharField(max_length=255)
    continent = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class WeaponType(models.Model):
    name = models.CharField(max_length=255)
    chinese_name = models.CharField(max_length=64)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Missile(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)
    weight = models.FloatField()
    diameter = models.FloatField()
    history = models.TextField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Ship(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.name
