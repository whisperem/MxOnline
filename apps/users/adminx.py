# coding=utf-8
__author__ = 'LXG'
__date__ = '2019/11/30 11:03'

import xadmin
from .models import EmailVerityRecord,Banner
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "爱学管理系统"
    site_footer = "爱学在线网"
    menu_style = "accordion"


class EmailVerityRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_type','send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url','index','add_time']
    search_fields = ['title', 'image','url','index']
    list_filter = ['title', 'image',  'url','index','add_time']


# class UsersAdmin(object):
#     list_display = ['nick_name', 'birthday', 'gender', 'address', 'mobile','image']
#     search_fields = ['nick_name', 'birthday', 'gender', 'address', 'mobile','image']
#     list_filter = ['nick_name', 'birthday', 'gender', 'address', 'mobile','image']


xadmin.site.register(EmailVerityRecord,EmailVerityRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
# xadmin.site.register(UserProfile,UsersAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)

