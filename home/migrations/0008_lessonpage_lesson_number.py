# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-11 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20170819_0906'),
        ('home', '0007_lessonpage_comments_for_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonpage',
            name='lesson_number',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
