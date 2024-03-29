# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-06-29 09:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App', '0001_initial'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('c_is_select', models.BooleanField(default=True)),
                ('goods', models.ForeignKey(db_column='goods', on_delete=django.db.models.deletion.CASCADE, related_name='gcartinfo', to='goods.GoodsInfo')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, related_name='ucartinfo', to='App.UserInfo')),
            ],
            options={
                'db_table': 'cartinfo',
            },
        ),
    ]
