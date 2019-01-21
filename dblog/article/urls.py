"""__author__ =侯晨皓"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from article import views



urlpatterns = [
    #path('add_acticle/',views.add_acticle,name='add_acticle'),
    path('article/',views.article,name='article'),

    path('add_art/',views.add_art,name='add_art'),
    path('del_art/',views.del_art,name='del_art'),
    path('up_art/<int:id>/',views.up_art,name='up_art'),





]

