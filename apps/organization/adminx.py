# -*- coding:utf-8 -*-
__author__ = 'LXG'
__date__ = '2019/11/30 16:19'

from .models import CityDict,CourseOrg,Teachers
import xadmin


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'addrsee', 'city','add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'addrsee', 'city']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'addrsee', 'city','add_time']


class TeachersAdmin(object):
    list_display = ['org','name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                    'add_time']
    search_fields = ['org','name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums']
    list_filter = ['org','name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums','add_time']





xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teachers,TeachersAdmin)



