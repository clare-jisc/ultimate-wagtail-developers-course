from django.db import models
from django.core.exceptions import ValidationError

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
    # internal url link to another page using wagtailcore.Page model
    cta_url = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # external url link to another page using django field
    cta_external_url = models.URLField(blank=True, null=True)

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
        MultiFieldPanel(
            [
                FieldPanel('cta_url'),
                FieldPanel('cta_external_url'),
            ],
            heading="Call to Action",
        ),
        FieldPanel('body'),
        FieldPanel('image'),
        FieldPanel('custom_document'),
        ]
    

    # custom method to get the url of the cta link
    @property
    def get_cta_url(self):
        if self.cta_url:
            return self.cta_url.url
        elif self.cta_external_url:
            return self.cta_external_url
        else:
            return None
        
    # apply custom validation to make sure only one of internal or external url is provided
    def clean(self):
        super().clean()

        if self.cta_url and self.cta_external_url:
            raise ValidationError({
                'cta_url': ValidationError("Please provide either an internal or external URL, not both", code='invalid'),
                'cta_external_url': ValidationError("Please provide either an internal or external URL, not both", code='invalid'),
            })
