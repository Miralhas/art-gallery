# Generated by Django 5.0 on 2023-12-22 01:28

import gallery.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_artwork_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='cover_photo',
            field=models.ImageField(blank=True, default='profile_pictures/default.jpg', null=True, upload_to=gallery.models.gallery_cover_photo_path),
        ),
    ]
