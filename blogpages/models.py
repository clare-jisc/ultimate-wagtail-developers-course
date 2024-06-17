from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


# Create your models here.
class BlogIndex(Page):
    # A listing page for all Blog detail pages
    template = "blogpages/blog_index_page.html"

    subtitle = models.CharField(max_length=100, blank=True, null=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("body"),
    ]


class BlogDetail(Page):
    # A listing page for all Blog detail pages
    template = "blogpages/blog_detail_page.html"

    subtitle = models.CharField(max_length=100, blank=True, null=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("body"),
    ]

