# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginRegisterApp', '0002_auto_20160718_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='Willard', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='Smith', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='ddddddddd', max_length=255),
            preserve_default=False,
        ),
    ]
