from datetime import datetime

from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,'Register.html')


def Deals_Detailed(request):

    return render(request,'Deals_Detailed.html')


def Help(request):

    return render(request,'Help.html')


def Preferential(request):
    return render(request,'Preferential.html')


def Product_list(request):
    return render(request,'Product_list.html')


def index(request):
    return render(request,'index.html')


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