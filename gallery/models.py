from django.db import models
from accounts.models import User

# Create your models here.

class Gallery(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="galleries")
    gallery_name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)


class Artwork(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name="artworks")
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="artworks/")
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)