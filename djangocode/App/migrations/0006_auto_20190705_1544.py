# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-05 07:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20190704_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='utimeCreate',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 5, 15, 44, 44, 745683)),
        ),
    ]
