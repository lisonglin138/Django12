"""djangocode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from App import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),

    url(r'^register/$',views.register,name="register"),
    url(r'^Deals_Detailed/$',views.Deals_Detailed,name="Deals_Detailed"),
    url(r'^Help/$',views.Help,name="Help"),
    url(r'^index/$',views.index,name="index"),
    url(r'^Preferential/$',views.Preferential,name="Preferential"),
    url(r'^Product_list/$',views.Product_list,name="Product_list"),
    url(r'^Products/$',views.Products,name="Products"),

    url(r'^Products_Detailed/$', views.Products_Detailed, name="Products_Detailed"),
    url(r'^Shopping_Cart/$', views.Shopping_Cart, name="Shopping_Cart"),
    url(r'^User_center/$', views.User_center, name="User_center"),
    url(r'^aa/$', views.aa, name="aa"),











]

