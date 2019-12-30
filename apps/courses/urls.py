# -*- coding:utf-8 -*-
__author__ = 'LXG'
__date__ = '2019/12/9 9:43'


from django.conf.urls import url,include
from organization.views import AddUserAskView
from courses.views import CourseListView,CourseDetailView,CourseInfoView,CommentView,AddCommentView,VideoPlayView


urlpatterns = [
    url(r'^list/$',CourseListView.as_view(),name="course_list"),
    url(r'^detail/(?P<course_id>\d+)/$',CourseDetailView.as_view(),name="course_detail"),
    url(r'^info/(?P<course_id>\d+)/$',CourseInfoView.as_view(),name="course_info"),
    url(r'^comment/(?P<course_id>\d+)/$',CommentView.as_view(),name="course_comment"),
    url(r'^add_comment/$',AddCommentView.as_view(),name="add_comment"),
    url(r'^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name="video_play"),

]