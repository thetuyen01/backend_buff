# Generated by Django 5.1 on 2024-08-18 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_alter_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='title_no_unidecode',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
