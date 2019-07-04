import hashlib
from datetime import datetime

from django.core.cache import cache
from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from App.forms import UserInfoForm, loginForm
from App.models import UserInfo, hCategory
from djangocode import settings

import logging

from goods.models import GoodsType

logger = logging.getLogger('django')





def register(request):


    if request.method =='POST':
        print(request.POST)
        print("--------1")
        form=UserInfoForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print("--------2")
            del form.cleaned_data['confirm_password']
            # 删除确认密码
            value =form.cleaned_data['upassword_has']
            form.cleaned_data['upassword_has']=hashlib.sha1(value.encode('utf8')).hexdigest()
            print(form.cleaned_data)
            # UserInfo.objects.create(uname=form.cleaned_data['uname'],upassword_has=form.cleaned_data['upassword_has'],uemail='826354949@qq.com')
            UserInfo.objects.create(**form.cleaned_data,uaddress=request.POST.get('uaddress'),uyoubian=request.POST.get('uyoubian'))
            print(UserInfo)
            return redirect(reverse('app:index'))

        # return render(request, 'Register.html')
        # uname = request.POST.get('username')
        # print(uname)

        return render(request, 'Register.html',context={'form':form})

    # return render(request,'Register.html',context={'uname_error':uname_error })



    else:
        form = UserInfoForm()

    return render(request,'Register.html')

def login(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        username = request.POST.get('uname')
        print(username)
        password = request.POST.get('upassword_has')
        password =hashlib.sha1(password.encode('utf8')).hexdigest()
        print(password)
        #搜索数据库
        res = UserInfo.objects.filter(uname=username,upassword_has=password)
        print(res)
        if res:
            request.session['uname']=username
            return redirect(reverse('app:index'))

    else:
        form = loginForm(request.POST)
    return render(request,'login.html',context={'form':form})


def Deals_Detailed(request):

    return render(request,'Deals_Detailed.html')


def Help(request):

    return render(request,'Help.html')


def Preferential(request):
    return render(request,'Preferential.html')


def Product_list(request):
    return render(request,'Product_list.html')

# 使用redis做缓存
def index(request):

    # 从缓存获取数据
    # data = cache.get()
    username=request.session.get('uname')
    # print(username)

    # 大板块遍历
    dbks = hCategory.objects.filter(hparentid='0').all()

    # 商品类型
    goodstypes=GoodsType.objects.filter(gparentid='0').all()

    # 此等商品类型
    list1=goodstypes.values('id')
    gt2s=GoodsType.objects.filter(gparentid__in= list1)
    # 具体商品
    list2 =gt2s.values('id')
    gt3s = GoodsType.objects.filter(gparentid__in=list2)
    print(list2)


    # print(res.values('hname'))
    hnames=dbks.values('hname')
    # 大板块下的小版块
    # 大于0的模块
    xbks=hCategory.objects.filter(hparentid__gt='0').all()


    # print(xbks)
    hparentid = xbks.values('hparentid')


    return render(request,'index.html',context={
        'title': '商城首页',
        'username':username,
        'hnames':hnames,
        'dbks':dbks,
        'goodstypes':goodstypes,
        'gt2s':gt2s,
        'gt3s': gt3s,

    })

def index1(request ,id):
    # 从缓存获取数据
    # data = cache.get()
    username = request.session.get('uname')
    # print(username)

    # 大板块遍历
    dbks = hCategory.objects.filter(hparentid='0').all()
    # print(res.values('hname'))
    hnames = dbks.values('hname')
    # 大板块下的小版块
    # 大于0的模块
    xbks = hCategory.objects.filter(hparentid__gt='0').all()
    # print(xbks)
    hparentid = xbks.values('hparentid')
    if request.method == 'GET':
        id = int(id)
        # 主页
        if id == 1:
            return render(request, 'index.html')
        # 蔬菜
        elif id == 2:
            # return render(request,'Products.html')
            return redirect(reverse('app:Products'))
        # 水果
        elif id == 3:
            # return render(request,'Products.html')
            return redirect(reverse('app:Products'))
        # 特价水果
        elif id == 4:
            # return render(request,'Products.html')
            return redirect(reverse('app:Products'))
        # 粮油
        elif id == 5:
            # return render(request,'Products.html')
            return redirect(reverse('app:Products'))
        # 套餐礼盒
        elif id == 6:
            # return render(request,'Products.html')
            return redirect(reverse('app:Products'))
        # 限时团购
        elif id == 7:
            # return render(request,'Products.html')
            return redirect(reverse('app:Products'))

    return render(request, 'index.html', context={
        'title': '商城首页',
        'username': username,
        'hnames': hnames,
        'dbks': dbks,
    })

def Products(request):
    return render(request,'Products.html')


def Products_Detailed(request):
    return render(request,'Products_Detailed.html')


def Shopping_Cart(request):
    return render(request,'Shopping_Cart.html')


def User_center(request):

    return render(request,'User_center.html')

# 测试用
def aa(request):
    return render(request,'linshicaozuo.html')




# 发送邮件
def send(request):
    send_mail('测试邮件','你好啊',settings.EMAIL_HOST_USER,['826253949@qq.com'])

    return HttpResponse('邮件发送成功')

# 群发邮件
def sendmany(request):
    m1 = ('测试邮件','不用回复',settings.EMAIL_HOST_USER,['562317408@qq.com',"landmark_csl@163.com"])
    m2 = ('测试邮件','不用回复',settings.EMAIL_HOST_USER,['313728420@qq.com',"landmark_csl@163.com"])
    m3 = ('测试邮件','不用回复',settings.EMAIL_HOST_USER,['826253949@qq.com',"landmark_csl@163.com"])

    send_mass_mail((m1, m2, m3),fail_silently=False)
    return HttpResponse('群发邮件')


# atthment 是激活邮件 带着附件信息过去
#  邮箱 需要设定    admin  需要改动
def attachment(request):
    subject,emial_from,to ='我是主题测试邮件',settings.EMAIL_HOST_USER,['826253949@qq.com']
    # 这是一个赋值语句，分别赋值主题   ， 发送者   ，接收者
    content=render(request,'active.html',context={'username':'admin'}).content
    content = content.decode('utf8')
    print(content)
    mail=EmailMultiAlternatives(subject=subject,from_email=emial_from,to=to)
    mail.attach_alternative(content,'text/html')
    mail.send()
    return HttpResponse('html邮件')

# 老师的代码
# def attachment(request):
#     subject,emial_from,to = '我是测试邮件',settings.EMAIL_HOST_USER,['826253949@qq.com']
#     content = render(request,'active.html',context={'username':'admin'}).content
#     content = content.decode('utf8')
#     print(content)
#     mail = EmailMultiAlternatives(subject=subject,from_email=emial_from,to=to)
#     mail.attach_alternative(content,'text/html')
#     mail.send()
#     return HttpResponse("html邮件")

def active(request):
    return None

# 富文本编辑器
def edit(request):
    if request.method == 'POST':
        print(request.POST.get('title'))
        print(request.POST.get('content'))



    return render(request,'edit.html')








