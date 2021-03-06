# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-19 09:02
from __future__ import unicode_literals

from django.db import migrations
import home.blocks.TabsBlock
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20171019_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultpage',
            name='body',
            field=wagtail.core.fields.StreamField((('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('audio', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.URLBlock()), ('downloadable', wagtail.core.blocks.BooleanBlock(required=False))))), ('video', wagtail.core.blocks.StructBlock((('source', wagtail.core.blocks.URLBlock()), ('poster', wagtail.core.blocks.URLBlock())))))),
        ),
        migrations.AlterField(
            model_name='lessonpage',
            name='body',
            field=wagtail.core.fields.StreamField((('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.URLBlock()),))), ('html', wagtail.core.blocks.RawHTMLBlock()), ('audio', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.URLBlock()), ('downloadable', wagtail.core.blocks.BooleanBlock(required=False))))), ('video', wagtail.core.blocks.StructBlock((('source', wagtail.core.blocks.URLBlock()), ('poster', wagtail.core.blocks.URLBlock())))))),
        ),
        migrations.AlterField(
            model_name='lessonpage',
            name='comments_for_lesson',
            field=wagtail.core.fields.StreamField((('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.URLBlock()),))), ('html', wagtail.core.blocks.RawHTMLBlock()), ('audio', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.URLBlock()), ('downloadable', wagtail.core.blocks.BooleanBlock(required=False))))), ('video', wagtail.core.blocks.StructBlock((('source', wagtail.core.blocks.URLBlock()), ('poster', wagtail.core.blocks.URLBlock()))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lessonpage',
            name='dictionary',
            field=wagtail.core.fields.StreamField((('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.URLBlock()),))), ('html', wagtail.core.blocks.RawHTMLBlock()), ('audio', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.URLBlock()), ('downloadable', wagtail.core.blocks.BooleanBlock(required=False))))), ('video', wagtail.core.blocks.StructBlock((('source', wagtail.core.blocks.URLBlock()), ('poster', wagtail.core.blocks.URLBlock())))), ('translations', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('word', wagtail.core.blocks.RichTextBlock(required=True)), ('translation', wagtail.core.blocks.RichTextBlock(required=True)))), template='blocks/transcriptions.html'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lessonpage',
            name='other_tabs',
            field=wagtail.core.fields.StreamField((('tab', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=True)), ('href', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.StreamBlock((('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.URLBlock()),))), ('html', wagtail.core.blocks.RawHTMLBlock()), ('audio', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.URLBlock()), ('downloadable', wagtail.core.blocks.BooleanBlock(required=False))))), ('video', wagtail.core.blocks.StructBlock((('source', wagtail.core.blocks.URLBlock()), ('poster', wagtail.core.blocks.URLBlock())))))))))),)),
        ),
        migrations.AlterField(
            model_name='pagewithsidebar',
            name='body',
            field=wagtail.core.fields.StreamField((('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.URLBlock()),))), ('html', wagtail.core.blocks.RawHTMLBlock()), ('audio', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.URLBlock()), ('downloadable', wagtail.core.blocks.BooleanBlock(required=False))))), ('video', wagtail.core.blocks.StructBlock((('source', wagtail.core.blocks.URLBlock()), ('poster', wagtail.core.blocks.URLBlock())))), ('tabs', home.blocks.TabsBlock.TabsBlock()), ('translations', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('word', wagtail.core.blocks.RichTextBlock(required=True)), ('translation', wagtail.core.blocks.RichTextBlock(required=True)))), template='blocks/transcriptions.html')))),
        ),
    ]
