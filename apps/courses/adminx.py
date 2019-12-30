# coding=utf-8
__author__ = 'LXG'
__date__ = '2019/11/30 12:44'

from .models import Course,Lesson,Video,CourseResource
import xadmin


class CourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_times','fav_nums','students','click_times','image','add_time']
    search_fields = ['name','desc','detail','degree','fav_nums','students','click_times','image']
    list_filter = ['name','desc','detail','degree','learn_times','fav_nums','students','click_times','image','add_time']


class LessonAdmin(object):
    list_display = ['course','name','add_time']
    search_fields = ['course','name']
    list_filter = ['course__name','name','add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download','add_time']
    search_fields = ['course', 'name','download']
    list_filter = ['course', 'name', 'download','add_time']


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)

