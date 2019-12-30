# -*- coding:utf-8 -*-
__author__ = 'LXG'
__date__ = '2019/12/17 8:38'


from django.conf.urls import url
from users.views import UserinfoView,UploadImageView,UpdatePwdView,SendEmailCodeView
from users.views import UpdateEmailView,MyCourseView,MyFavOrgView,MyFavTeacherView,MyFavCourseView,MymessageView

urlpatterns = [
    url(r'^info/$',UserinfoView.as_view(),name="user_info"),
    # yoghurt个人中心修改头像
    url(r'^image/upload/$',UploadImageView.as_view(),name="image_upload"),
    # 用户个人中心修改密码
    url(r'^update/pwd/$',UpdatePwdView.as_view(),name="update_pwd"),
    # 用户个人中心修改邮箱,发送验证码
    url(r'^sendemail_code/$',SendEmailCodeView.as_view(),name="sendemail_code"),

    # 用户个人中心修改邮箱
    url(r'^update_email/$',UpdateEmailView.as_view(),name="update_email"),

    # 用户课程
    url(r'^mycourse/$',MyCourseView.as_view(),name="mycourse"),

    # 我收藏的授课讲师
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name="myfav_teacher"),

    # 我收藏的课程
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),

    # 我的消息
    url(r'^mymessage/$', MymessageView.as_view(), name="mymessage"),

    # 用户收藏机构
    url(r'^myfav/org/$',MyFavOrgView.as_view(),name="myfav_org"),

]