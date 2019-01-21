"""__author__ =侯晨皓"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from user import views


#声明路由对象


urlpatterns = [
    path('index/',views.index,name='index'),
    path('login/',views.login,name='login'),

    path('add_user/',views.add_user,name='add_user'),
    path('del_user/',views.del_user,name='del_user'),
    path('up_user/',views.up_user,name='up_user'),
    path('sel_user/',views.sel_user,name='sel_user'),
    path('logout',views.logout,name='logout'),



    # 上传照片，不单独创建文件夹了
    path('photo/',views.photo,name='photo')


]

