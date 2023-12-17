from django.db import models
from django.urls import reverse

from accounts.models import User


def gallery_cover_photo_path(instance, filename):
    return 'user_{0}/gallery/cover_photo/{1}'.format(instance.owner.id, filename)

def gallery_artworks_path(instance, filename):
    return 'user_{0}/gallery/artworks/{1}'.format(instance.gallery.owner.id, filename)

# Create your models here.

class Gallery(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="galleries")
    gallery_name = models.CharField(max_length=255, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)
    cover_photo = models.ImageField(upload_to=gallery_cover_photo_path, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=False)

    def __str__(self):
        return self.gallery_name
    
    def get_absolute_path(self):
        return reverse("gallery:gallery", args=(self.owner.username, self.slug))


class Artwork(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name="artworks")
    title = models.CharField(max_length=255, null=True, blank=False)
    image = models.ImageField(upload_to=gallery_artworks_path, blank=False)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, blank=False, unique=True)

    def __str__(self):
        return f"{self.gallery} | {self.title}"
    
    # def get_absolute_path(self):
    #     return reverse("gallery:artwork", args=(self.slug, ))