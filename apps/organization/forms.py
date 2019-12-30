# -*- coding:utf-8 -*-
__author__ = 'LXG'
__date__ = '2019/12/6 10:01'
from django import forms
from operation.models import UserAsk
import re

class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name','mobile','course_name']

    def clean_mobile(self):
        """
        验证手机号是否合法，正则表达式
        """
        mobile = self.cleaned_data['mobile']
        test_mobile = "^1[35678]\d{9}$"
        p = re.compile(test_mobile)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码错误",code="mobile_invalid")



