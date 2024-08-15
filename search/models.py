from django.db import models
from django.utils.text import slugify

class Search(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Search, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
