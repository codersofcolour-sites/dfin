"""Flexible page."""
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, PageChooserPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks 
# Create your models here.


class FlexPage(Page):
    """Flexibile page class."""

    template = "flex/flex_page.html"

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
   )
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
        ],
        null=True,
        blank=True,
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
        FieldPanel("banner_title"),
        ImageChooserPanel("banner_image"),
        PageChooserPanel("banner_cta")

    ]

    class Meta:  # noqa 
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"

