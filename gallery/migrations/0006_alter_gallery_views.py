# Generated by Django 5.0 on 2023-12-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_gallery_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='views',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
