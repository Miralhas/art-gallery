# Generated by Django 5.0 on 2023-12-19 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
