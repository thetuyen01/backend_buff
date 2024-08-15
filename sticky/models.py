from django.db import models
from django.utils.text import slugify

class Sticky(models.Model):
    POSITION_CHOICES = (
        ('bottom', 'Bottom'),
        ('top', 'Top'),
        ('center', 'Center'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=2000, blank=True, null=True)
    url = models.CharField(max_length=2000)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Sticky, self).save(*args, **kwargs)

    def __str__(self):
        return self.title