# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-12 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_teachers_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='tag',
            field=models.CharField(default='全国知名', max_length=50, verbose_name='机构标签'),
        ),
    ]