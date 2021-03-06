# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-18 14:29
from __future__ import unicode_literals

import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion
from django.contrib.postgres.operations import HStoreExtension

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('infinitive', django.contrib.postgres.fields.hstore.HStoreField()),
                ('indicative', django.contrib.postgres.fields.hstore.HStoreField()),
                ('conditional', django.contrib.postgres.fields.hstore.HStoreField()),
                ('subjunctiv', django.contrib.postgres.fields.hstore.HStoreField()),
                ('imperative', django.contrib.postgres.fields.hstore.HStoreField()),
                ('participle', django.contrib.postgres.fields.hstore.HStoreField()),
            ],
        ),
        migrations.CreateModel(
            name='Verb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infinitive', models.CharField(max_length=100)),
                ('aspirated_h', models.BooleanField(default=False)),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conjugation.Template')),
            ],
        ),
    ]
