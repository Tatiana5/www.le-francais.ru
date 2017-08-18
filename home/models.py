from __future__ import absolute_import, unicode_literals

from django.db.models import CharField, SmallIntegerField, OneToOneField, BooleanField, SET_NULL
from django.forms import CheckboxInput

from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel, MultiFieldPanel
from wagtail.wagtailcore.blocks import RichTextBlock, RawHTMLBlock, ListBlock, StructBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.blocks import ImageChooserBlock

from pybb.models import Topic, Forum, Category

from home.blocks.AudioBlock import AudioBlock
from home.blocks.TabsBlock import TabsBlock, TabBlock


def is_nav_root(page: Page) -> bool:
    if isinstance(page, PageWithSidebar) and page.is_nav_root:
        return True
    if isinstance(page, LessonPage) and page.is_nav_root:
        return True
    else:
        return False


def get_nav_root(page: Page) -> Page:
    current_page = page
    while not is_nav_root(current_page):
        if current_page.get_parent() is None:
            break
        current_page = current_page.get_parent().specific
    return current_page


class DefaultPage(Page):
    body = StreamField([
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('html', RawHTMLBlock()),
        ('audio', AudioBlock())
    ])


DefaultPage.content_panels = Page.content_panels + [
    StreamFieldPanel('body'),
]


class PageWithSidebar(Page):
    is_nav_root = BooleanField(default=False)
    body = StreamField([
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('html', RawHTMLBlock()),
        ('audio', AudioBlock()),
        ('tabs', TabsBlock()),
        ('translations', ListBlock(StructBlock([
            ('word', RichTextBlock(required=True)),
            ('translation', RichTextBlock(required=True))
        ]), template="blocks/transcriptions.html")
         )
    ])

    def get_nav_root(self) -> Page:
        return get_nav_root(self)


PageWithSidebar.content_panels = Page.content_panels + [
    StreamFieldPanel('body'),
]

PageWithSidebar.settings_panels = PageWithSidebar.settings_panels + [
    FieldPanel('is_nav_root'),
]


class LessonPage(Page):
    is_nav_root = BooleanField(default=False)
    lesson_number = SmallIntegerField(blank=True, null=True)
    summary = CharField(max_length=100, null=True, blank=True)
    repetition_material = CharField(max_length=100, null=True, blank=True)
    audio_material = CharField(max_length=100, null=True, blank=True)
    comments_for_lesson = StreamField([
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('html', RawHTMLBlock()),
        ('audio', AudioBlock())
    ], null=True, blank=True)
    body = StreamField([
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('html', RawHTMLBlock()),
        ('audio', AudioBlock())
    ])
    dictionary = StreamField([
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('html', RawHTMLBlock()),
        ('audio', AudioBlock()),
        ('translations', ListBlock(StructBlock([
            ('word', RichTextBlock(required=True)),
            ('translation', RichTextBlock(required=True))
        ]), template="blocks/transcriptions.html")),
    ], null=True, blank=True)
    other_tabs = StreamField([('tab', TabBlock())])

    def get_lesson_number(self):
        return self.slug.split("lecon-", 1)[1]

    has_own_topic = BooleanField(default=False)
    topic = OneToOneField(
        Topic,
        on_delete=SET_NULL,
        null=True,
        blank=True
    )

    def get_nav_root(self) -> Page:
        return get_nav_root(self)


LessonPage.content_panels = Page.content_panels + [
    FieldPanel('audio_material'),
    StreamFieldPanel('comments_for_lesson'),
    StreamFieldPanel('body'),
    StreamFieldPanel('dictionary'),
    FieldPanel('summary'),
    FieldPanel('repetition_material'),
    StreamFieldPanel('other_tabs')
]

LessonPage.settings_panels = LessonPage.settings_panels + [
    FieldPanel('lesson_number'),
    FieldPanel('is_nav_root'),
    MultiFieldPanel(
        [
            FieldPanel('has_own_topic', widget=CheckboxInput),
            # FieldPanel('topic', widget=TopicForm),
        ],
        heading='Topic',
        classname='collapsible collapsed'
    )
]
