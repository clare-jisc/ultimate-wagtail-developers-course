from django.db import models
from django.core.exceptions import ValidationError

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model

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

    def get_context(self, request):
        # Update context to include only published BlogDetail pages
        context = super().get_context(request)
        blogpages = BlogDetail.objects.live().public()
        context["blogpages"] = blogpages
        return context


class BlogDetail(Page):
    # Blog detail page
    template = "blogpages/blog_detail_page.html"
    # parent and child page types allowed - empty list means no child pages allowed
    parent_page_types = ["blogpages.BlogIndex"]
    subpage_types = []

    subtitle = models.CharField(max_length=100, blank=True, null=True)
    body = RichTextField(blank=True)

    image = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("body"),
        FieldPanel("image"),
    ]


    # method to perform custom validation of fields
    def clean(self):
        super().clean() # call the default clean method() first

        # create empty dictionary to hold validation logic on the page
        # 'key: value' pairs where key is the field name and value is the error message
        validate = {}

        # example: do not allow the word blog to be used in the title, subtitle or slug
        if "blog" in self.title.lower():
            validate["title"] = "Title cannot have the word 'blog'"
        if "blog" in self.subtitle.lower():
            validate["subtitle"] = "Subtitle cannot have the word 'blog'"
        if "blog" in self.slug.lower():
            validate["slug"] = "Slug cannot have the word 'blog'"

        # if any validation errors raised show message on page
        if validate:
            raise ValidationError(validate)
        
