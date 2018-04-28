# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conjugation', '0016_verb_reflexive_no_accents'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReflexiveVerb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infinitive', models.CharField(max_length=100)),
                ('infinitive_no_accents', models.CharField(max_length=100)),
                ('deffective', models.BooleanField(default=False)),
                ('impersonal', models.BooleanField(default=False)),
            ],
        ),
    ]