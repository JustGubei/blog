from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.urls import reverse

from article.models import Photo
from user.forms import LoginForm
from user.models import User

from rest_framework import viewsets,mixins
from rest_framework.response import Response



#主页
def index(request):
    return render(request,'index.html')


# 登陆
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = User.objects.filter(username=username).first()

            if user:
                if password == user.password:
                    request.session['user_id'] = user.id
                    return HttpResponseRedirect(reverse('user:index'))

        else:
            msg = '账号或密码错误'
            return render(request,'login.html')














def add_user(request):
    user = User()
    user.username = '黎明'
    user.password = '123456'
    user.save()

    return HttpResponse('添加用户成功')

def del_user(request):

    User.objects.filter(username='黎明').first().delete()

    return HttpResponse('删除用户成功')

def up_user(request):

    user = User.objects.filter(username='黎明').first()
    user.username = '李白'
    user.password = '123123'
    user.save()

    return HttpResponse('更新用户成功')


def sel_user(request):

    user = User.objects.filter(username='李白').first()
    print(user.password)

    return HttpResponse('查询学生成功')


#
# def photo(request):
#     if request.method == 'POST':
#         new_img = Photo(
#             img=request.FILES.get('img'),
#             name = request.FILES.get('img').name
#         )
#         new_img.save()
#     return render(request, 'photo.html')
# #
def photo(request):
    if request.method == 'POST':
        new_img = Photo()
        new_img.img = request.FILES.get('img'),
        new_img.name = request.FILES.get('img').name
        new_img.save()
    return render(request, 'photo.html')



#退出

def logout(request):
    if request.method == 'GET':
        # 删掉session中的键值对
        del request.session['user_id']



        return HttpResponseRedirect(reverse('user:login'))

