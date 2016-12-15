# coding:utf8
from django.contrib import admin

from django.conf.urls import url

from myblog.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index)
]