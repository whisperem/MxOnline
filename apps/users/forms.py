# -*- coding:utf-8 -*-
from django import forms
# 这是一个验证码插件，第一步需要makemigrations生成验证码数据库表
from captcha.fields import CaptchaField
from .models import UserProfile

__author__ = 'LXG'
__date__ = '2019/12/3 10:38'

# 登录form过滤
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)

#引用验证码插件(注册)，注册form过滤
class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    captcha  = CaptchaField(error_messages={"invalid":u"验证码错误"})


# 忘记密码，增加验证码
class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha  = CaptchaField(error_messages={"invalid":u"验证码错误"})


# 修改密码表单过滤
class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True,min_length=5)
    password2 = forms.CharField(required=True,min_length=5)


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name','gender','birthday','address','mobile']
