# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-04 15:00
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20171204_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('document', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()),))), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('audio', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()), ('downloadable', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('video', wagtail.wagtailcore.blocks.StructBlock((('source', wagtail.wagtailcore.blocks.CharBlock()), ('poster', wagtail.wagtailcore.blocks.CharBlock(required=False))))))),
        ),
    ]