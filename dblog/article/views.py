from django.core.paginator import Paginator
from django.forms import Form
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
from django.urls import reverse




from rest_framework.routers import SimpleRouter
from rest_framework import viewsets,mixins
from rest_framework.response import Response

from article.models import Article, Category
from dblog.settings import ORDER_NUMBER


def article(request):
    if request.method == 'GET':
        art = Article.objects.all()



        page = int(request.GET.get('page', 1))
        pg = Paginator(art, ORDER_NUMBER)
        art = pg.page(page)

        return render(request,'article.html',{'art':art})




def add_art(request):
    if request.method == 'GET':
        cate = Category.objects.all()
        return render(request, 'add-article.html',{'cate':cate})
    if request.method == 'POST':

        art = Article()
        art.title = request.POST.get('title')
        art.content = request.POST.get('content')
        art.fid_id = request.POST.get('fid_id')
        art.save()

        return HttpResponseRedirect(reverse('article:article'))
#删除文章
def del_art(requset):
    if requset.method == 'POST':
        art_id = requset.POST.get('art_id')



        art = Article.objects.filter(pk=art_id).delete()




        return JsonResponse({'code':200,'msg':'删除成功'})







def up_art(request,id):
    if request.method == 'GET':

        art = Article.objects.filter(pk=id).first()
        category = Category.objects.filter(pk=art.fid_id).first()
        cate = Category.objects.all()
        return render(request,'update-article.html',{'category':category,'art':art,'cate':cate})

    if request.method == 'POST':


        article = Article.objects.filter(pk=id).first()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.fid_id = request.POST.get('fid_id')
        article.save()


        return HttpResponseRedirect(reverse('article:article'))





