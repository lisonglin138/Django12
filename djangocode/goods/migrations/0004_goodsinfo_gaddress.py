# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-05 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20190704_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsinfo',
            name='gaddress',
            field=models.CharField(max_length=128, null=True),
        ),
    ]