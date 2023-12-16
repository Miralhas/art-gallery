from django.db import models
from django.urls import reverse

from accounts.models import User

# Create your models here.

class Gallery(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="galleries")
    gallery_name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.gallery_name
    
    def get_absolute_path(self):
        return reverse("gallery:gallery", args=(self.owner.username, self.slug))


class Artwork(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name="artworks")
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="artworks/")
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title
    
    # def get_absolute_path(self):
    #     return reverse("gallery:artwork", args=(self.slug, ))