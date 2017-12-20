# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-04 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import home.blocks.TabsBlock
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_remove_page_draft_title'),
        ('home', '0015_auto_20171115_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('menu_title', models.TextField(blank=True)),
                ('reference_title', models.TextField(blank=True, null=True)),
                ('subtitle', models.TextField(blank=True, null=True)),
                ('body', wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('document', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()),))), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('audio', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()), ('downloadable', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('video', wagtail.wagtailcore.blocks.StructBlock((('source', wagtail.wagtailcore.blocks.CharBlock()), ('poster', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('post', wagtail.wagtailcore.blocks.StructBlock((('post_id', wagtail.wagtailcore.blocks.IntegerBlock()),)))))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='lessonpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('document', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()),))), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('audio', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()), ('downloadable', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('video', wagtail.wagtailcore.blocks.StructBlock((('source', wagtail.wagtailcore.blocks.CharBlock()), ('poster', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('post', wagtail.wagtailcore.blocks.StructBlock((('post_id', wagtail.wagtailcore.blocks.IntegerBlock()),))))),
        ),
        migrations.AlterField(
            model_name='lessonpage',
            name='comments_for_lesson',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('document', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()),))), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('audio', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()), ('downloadable', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('video', wagtail.wagtailcore.blocks.StructBlock((('source', wagtail.wagtailcore.blocks.CharBlock()), ('poster', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('post', wagtail.wagtailcore.blocks.StructBlock((('post_id', wagtail.wagtailcore.blocks.IntegerBlock()),)))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lessonpage',
            name='dictionary',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('document', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()),))), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('audio', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()), ('downloadable', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('video', wagtail.wagtailcore.blocks.StructBlock((('source', wagtail.wagtailcore.blocks.CharBlock()), ('poster', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('translations', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('word', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('translation', wagtail.wagtailcore.blocks.RichTextBlock(required=True)))), template='blocks/transcriptions.html')), ('post', wagtail.wagtailcore.blocks.StructBlock((('post_id', wagtail.wagtailcore.blocks.IntegerBlock()),)))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lessonpage',
            name='other_tabs',
            field=wagtail.wagtailcore.fields.StreamField((('tab', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('href', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('body', wagtail.wagtailcore.blocks.StreamBlock((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('document', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()),))), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('audio', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()), ('downloadable', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('video', wagtail.wagtailcore.blocks.StructBlock((('source', wagtail.wagtailcore.blocks.CharBlock()), ('poster', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('topic', wagtail.wagtailcore.blocks.StructBlock((('topic_id', wagtail.wagtailcore.blocks.IntegerBlock()),))), ('post', wagtail.wagtailcore.blocks.StructBlock((('post_id', wagtail.wagtailcore.blocks.IntegerBlock()),))))))))),)),
        ),
        migrations.AlterField(
            model_name='pagewithsidebar',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('document', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()),))), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('audio', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.CharBlock()), ('downloadable', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('video', wagtail.wagtailcore.blocks.StructBlock((('source', wagtail.wagtailcore.blocks.CharBlock()), ('poster', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('tabs', home.blocks.TabsBlock.TabsBlock()), ('translations', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('word', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('translation', wagtail.wagtailcore.blocks.RichTextBlock(required=True)))), template='blocks/transcriptions.html')), ('post', wagtail.wagtailcore.blocks.StructBlock((('post_id', wagtail.wagtailcore.blocks.IntegerBlock()),))))),
        ),
    ]