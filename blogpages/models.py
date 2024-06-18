from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


# Create your models here.
class BlogIndex(Page):
    # A listing page for all Blog detail pages
    template = "blogpages/blog_index_page.html"
    # number of index pages allowed
    max_count = 1
    # parent and child page types allowed
    parent_page_types = ["home.HomePage"]
    subpage_types = ["blogpages.BlogDetail"]

    subtitle = models.CharField(max_length=100, blank=True, null=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("body"),
    ]


class BlogDetail(Page):
    # Blog detail page
    template = "blogpages/blog_detail_page.html"
    # parent and child page types allowed - empty list means no child pages allowed
    parent_page_types = ["blogpages.BlogIndex"]
    subpage_types = []

    subtitle = models.CharField(max_length=100, blank=True, null=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("body"),
    ]
