# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-11-07 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20191101_1107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name_plural': '用户表'},
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
