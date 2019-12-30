# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=50,verbose_name=u"城市名字")
    desc = models.CharField(max_length=50,verbose_name=u"城市介绍")
    add_time = models.DateField(default=datetime.now,verbose_name=u"城市添加时间")

    class Meta:
        verbose_name = "城市信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 课程机构界面介绍
class CourseOrg(models.Model):
    name = models.CharField(max_length=50,verbose_name=u"机构名字")
    desc = models.TextField(max_length=500,verbose_name=u"机构介绍")
    tag = models.CharField(default='全国知名', max_length=50, verbose_name=u"机构标签")
    category = models.CharField(default="pxjg",max_length=20,verbose_name="所属类别",choices=(("pxjg","培训机构"),("gr","个人"),("gx","高校")))
    students =  click_nums = models.IntegerField(default=0,verbose_name=u"学生数")
    cources_num = models.IntegerField(default=0,verbose_name=u"课程数")
    click_nums = models.IntegerField(default=0,verbose_name=u"机构点击数")
    fav_nums  = models.IntegerField(default=0,verbose_name=u"机构被收藏次数")
    image = models.ImageField(max_length=100,upload_to="org/%Y/%m",verbose_name=u"logo")
    addrsee = models.CharField(max_length=200,verbose_name=u"机构所在地址")
    city = models.ForeignKey(CityDict,verbose_name=u"所在城市")
    add_time = models.DateField(default=datetime.now,verbose_name=u"机构添加时间")

    class Meta:
        verbose_name = "机构信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Teachers(models.Model):
    org = models.ForeignKey(CourseOrg,verbose_name="所属机构")
    name = models.CharField(max_length=50,verbose_name=u"教师名字")
    age = models.IntegerField(default=18,verbose_name="教师年龄")
    image = models.ImageField(default='',max_length=100,upload_to="teacher/%Y/%m",verbose_name=u"讲师")
    work_years = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50,verbose_name=u"工作公司")
    work_position = models.CharField(max_length=50,verbose_name=u"工作职位")
    points = models.CharField(max_length=50,verbose_name=u"教学特点")
    click_nums = models.IntegerField(default=0, verbose_name=u"教师点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"教师收藏次数")
    add_time = models.DateField(default=datetime.now,verbose_name=u"教师时间")

    class Meta:
        verbose_name = "教师信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name