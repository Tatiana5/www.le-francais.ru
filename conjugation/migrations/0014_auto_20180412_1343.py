# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-12 10:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conjugation', '0013_auto_20180412_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='verb',
            old_name='no_female',
            new_name='masculin_only',
        ),
    ]
