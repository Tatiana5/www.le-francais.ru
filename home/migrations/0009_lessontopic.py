# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-12 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        # ('pybb', '0007_auto_20170703_1731'),
        ('home', '0008_lessonpage_lesson_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonTopic',
            fields=[
                ('topic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='pybb.Topic')),
                ('lesson_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.LessonPage')),
            ],
            bases=('pybb.topic',),
        ),
    ]
