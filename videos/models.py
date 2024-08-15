from django.db import models
from categories.models import Category
from django.utils.text import slugify

class Video(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=2000, blank=True, null=True)
    url = models.CharField(max_length=2000)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Video, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
