"""pydcdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import myadmin
from . import dcapi

urlpatterns = [
    path('', myadmin.login),
    path('admin/', admin.site.urls),
    # path('hello/', myadmin.hello),
    # path('test/', myadmin.test),
    # path('testdata/', myadmin.testdata),
    path('foodadd/', myadmin.foodadd),
    path('foodaddpost/', myadmin.foodaddpost),
    path('foodlist/', myadmin.foodlist),
    path('foodedit/', myadmin.foodedit),
    path('foodeditpost/', myadmin.foodeditpost),
    path('fooddelete/', myadmin.fooddelete),
    path('orderlist/', myadmin.orderlist),
    path('orderdelete/', myadmin.orderdelete),
    path('orderview/', myadmin.orderview),
    path('login/', myadmin.login),
    path('loginpost/', myadmin.loginpost),
    path('cookeradd/', myadmin.cookeradd),
    path('cookeraddpost/', myadmin.cookeraddpost),
    path('cookerlist/', myadmin.cookerlist),
    path('cookeredit/', myadmin.cookeredit),
    path('cookereditpost/', myadmin.cookereditpost),
    path('cookerdelete/', myadmin.cookerdelete),
    path('newslist/', myadmin.newslist),
    path('viewpageradd/', myadmin.viewpageradd),
    path('viewpageraddpost/', myadmin.viewpageraddpost),
    path('viewpagerlist/', myadmin.viewpagerlist),
    path('viewpageredit/', myadmin.viewpageredit),
    path('viewpagereditpost/', myadmin.viewpagereditpost),
    path('viewpagerdelete/', myadmin.viewpagerdelete),
    path('dcapi/reg', dcapi.reg),
    path('dcapi/login', dcapi.login),
    path('dcapi/getfoodlist', dcapi.getfoodlist),
    path('dcapi/getfoodlistbyrandom', dcapi.getfoodlistbyrandom),
    path('dcapi/getfoodbyid', dcapi.getfoodbyid),
    path('dcapi/addtocar', dcapi.addtocar),
    path('dcapi/getcarlist', dcapi.getcarlist),
    path('dcapi/changecarnum', dcapi.changecarnum),
    path('dcapi/deleteitembyid', dcapi.deleteitembyid),
    path('dcapi/saveorder', dcapi.saveorder),
    path('dcapi/getcookerlistbyrandom', dcapi.getcookerlistbyrandom),
    path('dcapi/getnewslistbyrandom', dcapi.getnewslistbyrandom),
    path('dcapi/getviewpagerlistbyrandom', dcapi.getviewpagerlistbyrandom),
    path('dcapi/news', dcapi.news),
    path('dcapi/getorderlist', dcapi.getorderlist),
    path('dcapi/saveorder', dcapi.saveorder),
]
