# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-04 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_goodstype_gparentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodstype',
            name='gparentid',
            field=models.IntegerField(default=0),
        ),
    ]
