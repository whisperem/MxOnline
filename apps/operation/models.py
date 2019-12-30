# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from users.models import UserProfile
from courses.models import Course

from datetime import datetime
from django.db import models

# Create your models here.

# 最高一级，会根据用户的角度编写所需
#用户咨询
class UserAsk(models.Model):
    name = models.CharField(max_length=20,verbose_name=u"姓名")
    mobile = models.CharField(max_length=20,verbose_name=u"手机号")
    course_name= models.CharField(max_length=20,verbose_name=u"课程名")
    add_time = models.DateField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name


#用户评论
class CourseComment(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name=u"用户")
    course = models.ForeignKey(Course,verbose_name=u"课程")
    comments= models.CharField(max_length=200,verbose_name=u"评论")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "用户评论"
        verbose_name_plural = verbose_name

# 用户收藏
class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name=u"用户")
    # 节省字段，可以不再用外键，直接用即可
    fav_id = models.IntegerField(default=0,verbose_name=u"数据id")
    fav_type = models.IntegerField(choices=((1,"课程"),(2,"课程机构"),(3,"授课老师")),verbose_name=u"收藏类型")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name


#消息，页面短信通知
class UserMessage(models.Model):
    user = models.IntegerField(default=0,verbose_name=u"接受用户")
    message = models.CharField(max_length=500, verbose_name=u"消息内容")
    has_read = models.BooleanField(default=False,verbose_name=u"是否已读")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "界面消息提醒"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name=u"用户")
    course = models.ForeignKey(Course,verbose_name=u"课程")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course.name


