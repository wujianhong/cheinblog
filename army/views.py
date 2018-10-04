# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

# 另外写一个处理上传过来的文件的方法，并在这里导入
from somewhere import handle_uploaded_file


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)  # 注意获取数据的方式
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'army/upload.html', {'form': form})
