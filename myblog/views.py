# coding:utf8
from django.shortcuts import render, render_to_response

# Create your views here.
from myblog.models import *
from myblog.forms import CommentForm
from django.http import Http404
from myblog.models import Blog, Catagory

import datetime


def index(request):
    """
    初始界面,
    显示各分类排行 Category ranking,
    最近更新 Recent update,
    热门文章 Hot articles,
    """
    # get Category ranking
    catagory_ranking = []
    cata = Catagory.objects.all()
    count = 0
    for i in cata:
        a = Blog.objects.filter(catagory=i).count()
        i.name = str(i)
        if int(a) != 0:
            i.count = a
            catagory_ranking.append(i)
    catagory_ranking.sort(reverse=True)
    # get Recent update
    recent_update = []
    a = Blog.objects.order_by("-created")[0:5]
    for i in a :
        recent_update.append(i)
        recent_update.sort(reverse=True)
    # get Hot articles
    hot_articles = []
    b = Blog.objects.order_by("-chick")[0:5]
    for i in b :
        hot_articles.append(i)
    return render(request,'home_body.html',{'cata_list' : catagory_ranking[0:5], 'recent_list': recent_update, 'hot_list': hot_articles})


def get_blog_list(request):
    blog_list = []
    cata_id = request.GET.get('catagoryid')
    blog_type = Catagory.objects.get(id=cata_id)
    blog = Blog.objects.filter(catagory=cata_id).all()
    for i in blog:
        i.catagory = blog_type
        blog_list.append(i)
        clolor = '#1d8dcd'
    return render(request, 'blog_body.html', {'blog_list':blog_list})


def add_blog(request):
    if request.GET.get('blog'):
        print request.GET.get('blog')
    cata_list = Catagory.objects.all()
    for i in cata_list:
        print i
    return render(request,'text_edit.html', {'cata_list': cata_list})

def get_blog(request):
    blog_id = request.GET.get('id')
    blog_info = Blog.objects.get(id=blog_id)
    return render(request, 'blog_info.html', {'blog':blog_info})