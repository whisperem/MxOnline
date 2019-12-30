# -*- coding:utf-8 -*-
__author__ = 'LXG'
__date__ = '2019/12/6 10:02'

from django.conf.urls import url,include
from organization.views import OrgView,OrgHomeView,OrgCourseView,OrgDescView,OrgTeacherView,AddFavView
from organization.views import AddUserAskView,TeacherListView,TeacherDetailView


urlpatterns = [
    url(r'^list/$',OrgView.as_view(),name="org_list"),
    url(r'^add_ask/$',AddUserAskView.as_view(),name='add_ask'),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="org_home"),
    url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name="org_course"),
    url(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name="org_desc"),
    url(r'^org_teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name="org_teacher"),
    # 用户收藏,ajax
    url(r'^add_fav/$', AddFavView.as_view(), name="add_fav"),
    #教师列表
    url(r'^teacher/list/$', TeacherListView.as_view(), name="teacher_list"),
    url(r'^teacher/detail/(?P<teacher_id>\d+)/$', TeacherDetailView.as_view(), name="teacher_detail"),

]