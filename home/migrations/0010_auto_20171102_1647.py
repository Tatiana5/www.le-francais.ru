# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-02 13:47
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20171102_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indexreviewsreferences',
            old_name='review_subtitle',
            new_name='review_text',
        ),
        migrations.RenameField(
            model_name='indexreviewsreferences',
            old_name='referenced_review_url',
            new_name='review_url',
        ),
        migrations.RemoveField(
            model_name='indexreviewsreferences',
            name='referenced_review',
        ),
        migrations.RemoveField(
            model_name='indexreviewsreferences',
            name='review_title',
        ),
        migrations.AlterField(
            model_name='indexreviewsreferences',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='home.IndexPage'),
        ),
    ]
