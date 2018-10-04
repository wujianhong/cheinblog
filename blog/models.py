# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=30)
    eng_name = models.CharField(max_length=255)
    headImg = models.FileField(upload_to='./upload/')

    # 所以是用upload_to来指定文件存放的前缀路径

    def __str__(self):
        return self.name
