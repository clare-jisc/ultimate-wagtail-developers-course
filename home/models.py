from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    # Add model fields here
    subtitle = models.CharField(max_length=100, blank=True, null=True) 
    # Display model fields in admin UI
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
    ]
