# Generated by Django 5.1 on 2024-08-15 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_video_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
