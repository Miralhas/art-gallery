# Generated by Django 5.0 on 2023-12-18 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='stars',
            field=models.IntegerField(null=True),
        ),
    ]
