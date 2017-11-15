# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-15 10:24
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_indexreviews_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexreviews',
            name='external',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lessonpage',
            name='other_tabs',
            field=wagtail.wagtailcore.fields.StreamField((('tab', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('href', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('body', wagtail.wagtailcore.blocks.StreamBlock((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('document', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()),))), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('audio', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()), ('downloadable', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('video', wagtail.wagtailcore.blocks.StructBlock((('source', wagtail.wagtailcore.blocks.CharBlock()), ('poster', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('topic', wagtail.wagtailcore.blocks.StructBlock((('topic_id', wagtail.wagtailcore.blocks.IntegerBlock()),))))))))),)),
        ),
    ]