# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-06-29 09:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=20, unique=True)),
                ('ads', models.CharField(max_length=128, null=True)),
                ('aphone', models.CharField(default='18330066061', max_length=11)),
            ],
            options={
                'db_table': 'Address',
            },
        ),
        migrations.CreateModel(
            name='hCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20, unique=True)),
                ('hparentid', models.IntegerField(default=0)),
                ('hclasspath', models.CharField(max_length=128, null=True)),
            ],
            options={
                'db_table': 'hCategory',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20, unique=True)),
                ('upassword_has', models.CharField(max_length=40)),
                ('uemail', models.CharField(max_length=128, null=True)),
                ('isban', models.BooleanField(default=True)),
                ('isdelete', models.BooleanField(default=False)),
                ('uaddress', models.CharField(max_length=128, null=True)),
                ('uyoubian', models.CharField(max_length=6, null=True)),
                ('uphone', models.CharField(default='18330066061', max_length=11)),
                ('utimeCreate', models.DateTimeField(default=datetime.datetime(2019, 6, 29, 17, 34, 54, 929914))),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='zCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zname', models.CharField(max_length=20, unique=True)),
                ('zparentid', models.IntegerField(default=0)),
                ('zclasspath', models.CharField(max_length=128, null=True)),
            ],
            options={
                'db_table': 'zCategory',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.CASCADE, related_name='address', to='App.UserInfo'),
        ),
    ]
