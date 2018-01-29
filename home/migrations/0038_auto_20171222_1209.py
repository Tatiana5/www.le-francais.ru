# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-22 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import home.blocks.TabsBlock
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_auto_20171221_1822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placementadvertisementsnippet',
            old_name='placements',
            new_name='page_type',
        ),
        migrations.AddField(
            model_name='placementadvertisementsnippet',
            name='placement',
            field=models.CharField(choices=[('sidebar', 'Sidebar'), ('top', 'Top'), ('bottom', 'Bottom'), ('none', 'None')], default='none', max_length=100),
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('document', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()),))), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('audio', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()), ('downloadable', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('video', wagtail.wagtailcore.blocks.StructBlock((('source', wagtail.wagtailcore.blocks.CharBlock()), ('poster', wagtail.wagtailcore.blocks.CharBlock(required=False))))))),
        ),
        migrations.AlterField(
            model_name='lessonpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('document', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()),))), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('audio', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()), ('downloadable', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('video', wagtail.wagtailcore.blocks.StructBlock((('source', wagtail.wagtailcore.blocks.CharBlock()), ('poster', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('post', wagtail.wagtailcore.blocks.StructBlock((('post_id', wagtail.wagtailcore.blocks.IntegerBlock()),))))),
        ),
        migrations.AlterField(
            model_name='lessonpage',
            name='dictionary',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('document', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()),))), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('audio', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()), ('downloadable', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('video', wagtail.wagtailcore.blocks.StructBlock((('source', wagtail.wagtailcore.blocks.CharBlock()), ('poster', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('translations', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('word', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('translation', wagtail.wagtailcore.blocks.RichTextBlock(required=True)))), template='blocks/transcriptions.html')), ('post', wagtail.wagtailcore.blocks.StructBlock((('post_id', wagtail.wagtailcore.blocks.IntegerBlock()),)))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pagewithsidebar',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('document', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()),))), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('audio', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()), ('downloadable', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('video', wagtail.wagtailcore.blocks.StructBlock((('source', wagtail.wagtailcore.blocks.CharBlock()), ('poster', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('tabs', home.blocks.TabsBlock.TabsBlock()), ('translations', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('word', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('translation', wagtail.wagtailcore.blocks.RichTextBlock(required=True)))), template='blocks/transcriptions.html')), ('post', wagtail.wagtailcore.blocks.StructBlock((('post_id', wagtail.wagtailcore.blocks.IntegerBlock()),))), ('choosen_reviews', wagtail.wagtailcore.blocks.StructBlock(())))),
        ),
        migrations.AlterField(
            model_name='placementadvertisementsnippet',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('html', wagtail.wagtailcore.blocks.RawHTMLBlock()),), blank=True),
        ),
    ]