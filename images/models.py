from django.db import models
from wagtail.images.models import Image, AbstractImage, AbstractRendition

# Create your models here.
# Need to add Custom image model to blog/settings/base.py as WAGTAILIMAGES_IMAGE_MODEL = 'images.CustomImage'
class CustomImage(AbstractImage):
    # Add any extra fields to image here

    # eg. To add a caption field:
    caption = models.CharField(max_length=255, blank=True)

    admin_form_fields = Image.admin_form_fields + ('caption',)

class CustomRendition(AbstractRendition):
    image = models.ForeignKey(CustomImage, on_delete=models.CASCADE, related_name='renditions')

    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )
