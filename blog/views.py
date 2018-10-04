# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from xpinyin import Pinyin
from django.shortcuts import render, render_to_response
from django import forms  # 重点要导入,使用 Django 的 表单
from django.http import HttpResponse
from .models import Image


class ImageForm(forms.Form):
    name = forms.CharField()  # 字符串
    headImg = forms.FileField()  # 文件


'''
函数判断用户的是否为POST请求，如果是并验证是有效的，然后就返回upload ok!，在验证正确和返回OK的中间放我们的上传文件代码，因为只有文件上传成功能返回OK，我们一会说，如果是GET请求，就直接显示一个空表单，让用户输入。
'''


def upload(request):
    if request.method == "POST":
        uf = ImageForm(request.POST, request.FILES)
        if uf.is_valid():
            name = uf.cleaned_data["name"]
            eng_name = Pinyin().get_pinyin(name, "_").replace(" ", "_")
            head_img = uf.cleaned_data["headImg"]
            image = Image()
            image.name = name
            image.eng_name = eng_name
            image.headImg = head_img
            image.save()
            return HttpResponse("Upload OK !")

    else:
        uf = ImageForm()
    return render_to_response('army/upload.html', {"uf": uf})
