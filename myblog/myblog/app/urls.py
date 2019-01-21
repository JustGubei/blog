from django.urls import path

from app import views
urlpatterns = [
    # 首页
    path('index/', views.index, name='index'),
    # 相册
    path('share/', views.share, name='share'),
    # 日记
    path('list/', views.list, name='list'),

    # 内容页
    path('info_pic/', views.info_pic, name='info_pic'),
    # 留言
    path('g_book/', views.g_book, name='g_book'),
    # 内容页
    path('info/<int:id>/', views.info, name='info'),




]