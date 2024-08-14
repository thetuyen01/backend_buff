from django.db import models
from categories.models import Category

class Video(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=2000, blank=True, null=True)
    url = models.CharField(max_length=2000)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
