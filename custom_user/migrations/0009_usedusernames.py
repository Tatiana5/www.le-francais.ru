# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-02 09:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0008_auto_20171017_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsedUsernames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('used_username', models.CharField(max_length=32)),
                ('change_datetime', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
