# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

#个人信息用户表
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name=u"昵称",default="")
    birthday = models.DateField(verbose_name=u"生日",null=True,blank=True)
    gender = models.CharField(max_length=8,choices=(("male",u"男"),("female","女")),default="female")
    address = models.CharField(max_length=100,default=u"")
    mobile = models.CharField(max_length=20,null=True,blank=True)
    image = models.ImageField(upload_to="media/%Y/%m",default=u"media/1.png",max_length=100)
    # email = models.EmailField(max_length=50, verbose_name=u"邮箱")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


#邮箱验证码和忘记密码验证码
class EmailVerityRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name=u"验证码")
    email = models.EmailField(max_length=50,verbose_name=u"邮箱")
    #判断是邮箱验证码，还是忘记密码验证码
    send_type = models.CharField(verbose_name=u"验证类型",choices=(("register",u"注册"),("forget",u"忘记密码"),("update_email",u"修改邮箱")),max_length=50)
    send_time = models.DateField(verbose_name=u"发送时间",default=datetime.now)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}{1}'.format(self.code,self.email)
#轮播图表
class Banner(models.Model):
    title = models.CharField(max_length=50,verbose_name=u"轮播图标题")
    image = models.ImageField(max_length=100,verbose_name=u"图片",upload_to="banner/%Y/%m")
    # 点击图片跳转路径
    url = models.URLField(max_length=100,verbose_name=u"访问地址")
    # 轮播图图片位置顺序
    index = models.IntegerField(default=100,verbose_name=u"轮播顺序")
    add_time = models.DateField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name
