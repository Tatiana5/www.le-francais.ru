# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-26 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conjugation', '0028_auto_20180426_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_rus', models.CharField(default='', max_length=1000)),
                ('text_fr', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]
