# coding:utf8
from django.contrib import admin

from django.conf.urls import url,include

from myblog.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index),
    url(r'^python/(.+)/$', get_blog),
]