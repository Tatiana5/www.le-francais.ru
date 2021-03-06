# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-16 13:54
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conjugation', '0003_auto_20180316_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='conditional',
        ),
        migrations.RemoveField(
            model_name='template',
            name='imperative',
        ),
        migrations.RemoveField(
            model_name='template',
            name='indicative',
        ),
        migrations.RemoveField(
            model_name='template',
            name='infinitive',
        ),
        migrations.RemoveField(
            model_name='template',
            name='participle',
        ),
        migrations.RemoveField(
            model_name='template',
            name='subjunctive',
        ),
        migrations.AddField(
            model_name='template',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
    ]
