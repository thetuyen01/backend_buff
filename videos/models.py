from django.db import models
from categories.models import Category
from django.utils.text import slugify
from unidecode import unidecode

class Video(models.Model):
    VIDEO_TYPE_CHOICES = [
        ('server1', 'Server1'),
        ('server2', 'Server2'),
    ]
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    title_no_unidecode = models.CharField(max_length=200, blank=True, null=True)
    image = models.CharField(max_length=2000, blank=True, null=True)
    # server1
    url = models.CharField(max_length=2000, blank=True, null=True)
    iframe = models.CharField(max_length=2000, blank=True, null=True)
    # server2
    url2 = models.CharField(max_length=2000, blank=True, null=True)
    iframe2 = models.CharField(max_length=2000, blank=True, null=True)

    type = models.CharField(max_length=100, choices=VIDEO_TYPE_CHOICES, default='server1')

    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    likes = models.IntegerField(default=159)
    dislikes = models.IntegerField(default=145)
    views = models.IntegerField(default=10)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        self.title_no_unidecode = unidecode(self.title).lower()
        super(Video, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
