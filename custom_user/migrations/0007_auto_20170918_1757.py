# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-18 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0006_auto_20170918_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that nickname already exists.'}, help_text='Your forum nickname (can be changed later)', max_length=32, unique=True, verbose_name='nickname'),
        ),
    ]