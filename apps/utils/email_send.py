# -*- coding:utf-8 -*-
__author__ = 'LXG'
__date__ = '2019/12/3 20:38'
import random
from users.models import EmailVerityRecord
from django.core.mail import send_mail
from MxOnline.settings import EMAIL_FROM

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars)-1
    for i in range(randomlength):
        str += chars[random.randint(0,length)]
    return str


def send_register_email(email,send_type="reqister"):
    email_record = EmailVerityRecord()
    if send_type=="update_email":
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()


    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "乐学在线网注册激活链接,有效期两分钟"
        email_body = "点击下面的链接激活您的账号：http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            pass

    elif send_type == "forget":
        email_title = "乐学在线网修改密码链接,有效期两分钟"
        email_body = "点击下面的链接修改您的密码：http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            pass
    elif send_type == "update_email":
        email_title = "慕课网在线邮箱修改验证码,有效期两分钟"
        email_body = "您的邮箱验证码为：{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass