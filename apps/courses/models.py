# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from datetime import datetime

from organization.models import CourseOrg,Teachers
# Create your models here.


#课程models

class Course(models.Model):

    course_org = models.ForeignKey(CourseOrg,verbose_name="课程机构",null=True,blank=True)

    # 广告位轮播
    is_banner = models.BooleanField(default=False,verbose_name="是否轮播")
    name = models.CharField(max_length=50,verbose_name=u"课程名")
    desc = models.CharField(max_length=300,verbose_name=u"课程描述")
    teacher = models.ForeignKey(Teachers,max_length=20,verbose_name="授课讲师",null=True,blank=True)
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(max_length=20,choices=(("cj",u"初级"),("zj","中级"),("gj","高级")))
    learn_times = models.IntegerField(default=0,verbose_name=u"学习时间(分钟算)")
    students = models.IntegerField(default=0,verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0,verbose_name=u"收藏人数")
    click_times = models.IntegerField(default=0,verbose_name=u"点击数")
    category = models.CharField(default='',max_length=20,verbose_name=u"课程类别")
    image = models.ImageField(max_length=100,upload_to="cources/%Y/%m",verbose_name=u"课程封面")
    add_time = models.DateField(default=datetime.now,verbose_name=u"课程添加时间")
    tag = models.CharField(default='', max_length=20, verbose_name=u"课程标签")
    you_need_know = models.TextField(verbose_name=u"课程须知",default="")
    teacher_tell_you = models.TextField(verbose_name=u"老师告诉你",default="")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_zj_num(self):
        return self.lesson_set.all().count()

    def get_learn_user(self):
        return self.usercourse_set.all()[:5]

    def get_course_num(self):
        return self.lesson_set.all().count()

    def get_teacher_num(self):
        return self.course_org.teachers_set.all().count()

    def get_course_lesson(self):
        return self.lesson_set.all()

# 章节表设计
class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name=u"课程")
    name = models.CharField(max_length=100,verbose_name="章节名")
    add_time = models.DateField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def get_lesson_video(self):
        return self.video_set.all()

    def __str__(self):
        return self.name


# 章节里面的视频表
class Video(models.Model):
    lesson = models.ForeignKey(Lesson,verbose_name=u"章节")
    name = models.CharField(max_length=100,verbose_name="视频名")
    url = models.CharField(max_length=200, verbose_name="视频地址", default="")
    learn_times = models.IntegerField(default=0,verbose_name=u"学习时间(分钟算)")
    add_time = models.DateField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 课程页面右侧的资源下载
class CourseResource(models.Model):
    course = models.ForeignKey(Course,verbose_name=u"课程")
    name = models.CharField(max_length=100,verbose_name="章节名")
    download = models.FileField(upload_to="course/%Y/%m",verbose_name="资源下载")
    add_time = models.DateField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"资源下载"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



