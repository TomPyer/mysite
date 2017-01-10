# coding:utf8
from django.contrib import admin
from django.conf.urls import url,include
from django.views.static import serve
from myblog.views import *
from mysite import settings
from views import view_cla


view_obj = view_cla()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', view_obj.index),
    url(r'^python/', view_obj.get_blog_list),
    url(r'^static/(?P<path>.*)$', serve,{ 'document_root': settings.STATIC_URL }),
    url(r'^add_blog/$', view_obj.add_blog),
    url(r'^get_blog/$', view_obj.get_blog),
    # url(r'^search_blog/$', view_obj.search_blog)
]