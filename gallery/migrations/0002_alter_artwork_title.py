# Generated by Django 5.0 on 2023-12-17 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
