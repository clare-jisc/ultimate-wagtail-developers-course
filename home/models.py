from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, HelpPanel
from wagtail.fields import RichTextField

from wagtail.images import get_image_model
from wagtail.documents import get_document_model

class HomePage(Page):
    # set template location for page, not usually needed on model class as default from Page model
    # is needed on snippet models!!
    template = "home/home_page.html" 
    # number of home pages allowed
    max_count = 1

    # Add model fields here
    info = models.TextField(blank=True)
    subtitle = models.CharField(max_length=100, blank=True, null=True) 
    body = RichTextField(blank=True)

    # use invoked function to access both "images.CustomImage" model and "wagtailimages.Image" model
    image = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    custom_document = models.ForeignKey(
        get_document_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Display model fields in admin UI
    # standard FieldPanel now covers all types of field eg RichTextField
    content_panels = Page.content_panels + [
        FieldPanel('info', read_only=True),
        MultiFieldPanel(
            [
                HelpPanel("Don't forget to check the box on promote tab to show in menus", heading="editor tips"),
            ],
            heading="Helpful Hints",
        ),
        FieldPanel('subtitle'),
        FieldPanel('body'),
        FieldPanel('image'),
        FieldPanel('custom_document'),
    ]
