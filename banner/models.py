from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=2000)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
