# coding:utf8
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Catagory(models.Model):
    """
    博客分类
    """
    name = models.CharField('名称',max_length=30)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    """
    博客标签
    """
    name = models.CharField('名称',max_length=72)

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    """
    博客
    """
    title = models.CharField('标题',max_length=32)
    author = models.CharField('作者',max_length=100)
    content = models.TextField('博客正文')
    created = models.DateTimeField('发布时间',auto_now_add=True)
    catagory = models.ForeignKey(Catagory,verbose_name='分类')
    tag = models.ForeignKey(Tag,verbose_name='标签')
    chick = models.IntegerField('点击数', default=0)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    """
    评论
    """
    blog = models.ForeignKey(Blog,verbose_name='博客')
    name = models.CharField('称呼',max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容',max_length=240)
    created = models.DateTimeField('发布时间',auto_now_add=True)

    def __unicode__(self):
        return self.content


class Grade(models.Model):
    """
    用户等级
    """
    grade_name = models.CharField('等级标识', max_length=60)

    def __unicode__(self):
        return self.grade_name


class User(models.Model):
    """
    用户
    """
    name = models.CharField('用户名', max_length=40)
    password = models.CharField('密码', max_length=18)
    email = models.EmailField('邮箱')
    phone = models.CharField('电话', max_length=18)
    created = models.DateTimeField('注册时间', auto_now_add=True)
    grade = models.ForeignKey(Grade, verbose_name='等级标识')

    def __unicode__(self):
        return self.name
