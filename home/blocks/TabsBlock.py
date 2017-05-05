from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks.field_block import RichTextBlock, RawHTMLBlock, CharBlock
from wagtail.wagtailcore.blocks.stream_block import StreamBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from home.blocks.AudioBlock import AudioBlock


class TabsBlock(blocks.ListBlock):
    def __init__(self):
        super(TabsBlock, self).__init__(TabBlock)

    class Meta:
        template = 'blocks/tabs.html'


class TabBlock(blocks.StructBlock):
    title = CharBlock(required=True)
    href = CharBlock(required=True)
    body = StreamBlock([
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('html', RawHTMLBlock()),
        ('audio', AudioBlock())
    ])

    # class Meta:
    #     template = 'blocks/audio_player.html'