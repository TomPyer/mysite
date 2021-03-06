# coding:utf8
from django.shortcuts import render, render_to_response

# Create your views here.
from myblog.models import *
from myblog.forms import CommentForm
from django.http import Http404
from myblog.models import Blog, Catagory

import datetime
import jieba
import urllib


class view_cla(object):
    def __init__(self):
        pass

    def index(self, request):
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

    def get_blog_list(self, request):
        blog_list = []
        cata_id = 0
        if request.GET.get('catagoryname') is not None:
            c_name = request.GET.get('catagoryname')
            cata_id = Catagory.objects.get(name=c_name).id
        elif request.GET.get('catagoryid') is not None:
            cata_id = request.GET.get('catagoryid')
        blog_type = Catagory.objects.get(id=cata_id)
        blog = Blog.objects.filter(catagory=cata_id).all()
        for i in blog:
            i.catagory = blog_type
            blog_list.append(i)
        return render(request, 'blog_body.html', {'blog_list':blog_list})

    def add_blog(self, request):
        catagory_list = Catagory.objects.all()
        dic_tag = {'life':1, 'sepro':2, 'study':3, 'skill':4}
        if request.method == "GET":
            if request.GET.get('tag') is not None:
                blog_obj = request.GET
                print blog_obj.get('blog')
                tag_id = dic_tag[blog_obj.get('tag')]
                cata_id = Catagory.objects.get(name=blog_obj.get('catagory'))
                b = Blog(title= blog_obj.get('title'),
                         author='tangxuelin',
                         content=blog_obj.get('blog'),
                         created=datetime.datetime.now(),
                         catagory_id=cata_id.id,
                         tag_id=int(tag_id))
                b.save()
        elif request.POST:
            print request.POST['title']
            print request.POST['catagory']
            print request.POST['tags']
            print request.POST['content']
            tag_id = dic_tag[request.POST['tags']]
            cata_id = Catagory.objects.get(name=request.POST['catagory'])
            b = Blog(title= request.POST['title'],
                     author='tangxuelin',
                     content=request.POST['content'],
                     created=datetime.datetime.now(),
                     catagory_id=cata_id.id,
                     tag_id=int(tag_id))
            b.save()

        return render(request,'text_edit_2.html', {'cata_list': catagory_list})

    def get_blog(self, request):
        blog_id = request.GET.get('id')
        blog_info = Blog.objects.get(id=blog_id)
        blog_info.chick += 1
        blog_info.save()
        return render(request, 'blog_info.html', {'blog':blog_info})

    def search_blog(self, request):
        select_title_value = []
        select_body_value = []
        select_author_value = []
        x = request.GET.get('select_key')
        blog_list = Blog.objects.all()
        for i in blog_list:
            if x in i.title:
                select_title_value.append(i)
                continue
            if x in i.content:
                select_body_value.append(i)
                continue
            if x in i.author:
                select_author_value.append(i)

        select_title_total = len(select_title_value)
        select_body_total = len(select_body_value)
        select_author_total = len(select_author_value)
        select_all_value = select_title_value + select_body_value + select_author_value
        select_all_total = select_title_total + select_body_total + select_author_total
        select_all_status = 'error' if len(select_all_value) == 0 else 'success'
        return render(request, 'search.html', {"select_all":select_all_value,
                                               "select_status":select_all_status,
                                               "select_total": select_all_total,
                                               "title_total": select_title_total,
                                               "body_total": select_body_total,
                                               "author_total":select_author_total,
                                               "select_key": x,
                                               })