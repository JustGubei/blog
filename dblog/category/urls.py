"""__author__ =侯晨皓"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from category import views



urlpatterns = [


    path('category/',views.category,name='category'),
    #删除
    path('del_cate/',views.del_cate,name='del_cate'),


]

