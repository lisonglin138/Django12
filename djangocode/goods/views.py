from datetime import datetime
import os
from random import randint

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from djangocode import settings



# 问题  不知道为啥文件夹不可以递归创建
def upload1(request):
    if request.method == 'POST':
    # photo 是表单中文件上传的name
        file = request.FILES.get('photo')
        print(file)
        # 文本路径
        path = os.path.join(settings.MEDIA_ROOT,file.name)
        # 文件类型过滤
        ext = os.path.splitext(file.name)
        print(ext)
        print('----------1')
        print(len(ext) < 1)
        print(ext[1] in settings.ALLOWED_FILEEXTS)
        # if len(ext) < 1 or not ext[1] in settings.ALLOWED_FILEEXTS:
        if len(ext) < 1 or not ext[1] in settings.ALLOWED_FILEEXTS:
            print('----------2')
            return redirect(reverse('goods:upload1'))
        # 解决文件重名
        print(os.path.exists(path))
        if os.path.exists(path):
            print('----------3')
            #日期目录
            dir = datetime.today().strftime("%Y%m%d")
            dir = os.path.join(settings.MEDIA_ROOT,dir)
            print(dir)
            if not os.path.exists(dir):
                os.makedirs(dir) #递归创建目录

        file_name=ext[0] + datetime.today().strftime("%Y%m%d%H%M%S") + str(randint(1,1000)) + ext[1] if len(ext) > 1 else ''
        path = os.path.join(dir,file_name)
        print(path)
        #创建文件
        with open(path,'wb') as fp:
            print('----------4')
            #如果文件超过2.5 M ，则分块读写
            if file.multiple_chunks():
                for block1 in file.chunks():
                    fp.write(block1)
            else:
                fp.write(file.read())
        return HttpResponse('图片上传成功')
    print('----------5')
    return render(request,'wenjianshangchuan.html')























