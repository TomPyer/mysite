# coding:utf8
from django.contrib import admin
from django.conf.urls import url,include
from django.views.static import serve
from myblog.views import *
from mysite import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index),
    url(r'^python/(.+)/$', get_blog),
    url( r'^static/(?P<path>.*)$', serve,{ 'document_root': settings.STATIC_URL }),
]