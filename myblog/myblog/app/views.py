from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Category, Article, Photo
from myblog.settings import ORDER_NUMBER


def index(request):
    '''
    首页渲染
    :param request:
    :return:
    '''
    if request.method == 'GET':
        art = Article.objects.all()
        category = Category.objects.all()
        photo = Photo.objects.filter(id__lte=15)
        blogs = Article.objects.all().order_by('-update_time')[:3]

        return render(request, 'index.html',
                      {'art':art,
                       'blogs':blogs,
                       'category':category,
                       'photo':photo,

                       })

def share(request):
    '''
    相册
    :param request:
    :return:
    '''

    if request.method == 'GET':
        imgs = Photo.objects.all()

        page = int(request.GET.get('page', 1))
        pg = Paginator(imgs, ORDER_NUMBER)
        imgs = pg.page(page)

        return render(request, 'share.html',{'imgs':imgs})

def list(request):
    """
    日记
    :param request:
    :return:
    """

    if request.method == 'GET':
        blogs = Article.objects.all()
        category = Category.objects.all()
        return render(request, 'list.html',{'blogs':blogs, 'category':category})




def info_pic(request):
    '''
    内容页
    :param request:
    :return:
    '''
    if request.method == 'GET':
        blogs = Article.objects.all()
        category = Category.objects.all()
        photo = Photo.objects.filter(id__lte=15)
        return render(request, 'infopic.html',{'blogs':blogs, 'category':category,'photo':photo})


def info(request,id):
    '''
    内容页
    :param request:
    :return:
    '''

    if request.method == 'GET':
        art = Article.objects.filter(pk=id).first()
        blogs = Article.objects.all()
        category = Category.objects.all()

        #点击量加一
        click = art.click_num
        art.click_num = click + 1
        art.save()

        #排行
        arts = Article.objects.all().order_by('-click_num')[:3]


        return render(request, 'info.html',{'blogs':blogs, 'category':category,'art':art,'arts':arts})

def g_book(request):
    '''
    内容页
    :param request:
    :return:
    '''

    if request.method == 'GET':
        blogs = Article.objects.all()
        category = Category.objects.all()
        photo = Photo.objects.filter(id__lte=15)
        return render(request, 'gbook.html',{'blogs':blogs, 'photo':photo})



