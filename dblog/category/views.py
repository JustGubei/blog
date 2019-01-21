from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from article.models import Category


def category(request):
    if request.method == 'GET':
        cate = Category.objects.all()
        return render(request,'category.html',{'cate':cate})

    if request.method == 'POST':
        lmmc = request.POST.get('name')

        cate1 = Category()

        cate1.lmmc = lmmc
        cate1.save()

        cate = Category.objects.all()


        return render(request,'category.html',{'cate':cate})


def del_cate(request):
    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')

        cart = Category.objects.filter(pk=cart_id).delete()

        return JsonResponse({'code': 200, 'msg': '删除成功'})




