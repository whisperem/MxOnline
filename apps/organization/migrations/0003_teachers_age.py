# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-11 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_teachers_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='age',
            field=models.IntegerField(default=18, verbose_name='教师年龄'),
        ),
    ]