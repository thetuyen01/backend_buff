# Generated by Django 5.1 on 2024-08-13 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
