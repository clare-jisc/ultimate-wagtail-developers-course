from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, HelpPanel
from wagtail.fields import RichTextField

class HomePage(Page):
    # set template location for page, not usually needed on model class as default from Page model
    # is needed on snippet models!!
    template = "home/home_page.html"
    # Add model fields here
    subtitle = models.CharField(max_length=100, blank=True, null=True) 
    body = RichTextField(blank=True)
    info = models.TextField(blank=True)

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
    ]
