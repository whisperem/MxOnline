# -*- coding:utf-8 -*-
__author__ = 'LXG'
__date__ = '2019/11/30 16:37'


from .models import UserAsk,CourseComment,UserFavorite,UserMessage,UserCourse
import xadmin


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name','add_time']
    search_fields = ['name', 'mobile','course_name']
    list_filter = ['name', 'mobile', 'course_name','add_time']


class CourseCommentAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time','image']
    search_fields = ['user', 'course', 'has_read','image']
    list_filter = ['user', 'course','add_time','image']


xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(CourseComment,CourseCommentAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)