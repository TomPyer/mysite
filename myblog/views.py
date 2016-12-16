from django.shortcuts import render, render_to_response

# Create your views here.
from myblog.models import *
from myblog.forms import CommentForm
from django.http import Http404


def index(request):
        return render_to_response('home_body.html')


def get_blog(request, blog_type):
    return render_to_response('%s.html'%blog_type)