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
    views = models.IntegerField(default=0)

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
    views = models.IntegerField(default=0)


    @property
    def review_status(self):
        reviews = self.comments.all()

        # status
        total_reviews = len(reviews)
        try:
            rating = sum([review.stars for review in reviews]) // total_reviews
        except ZeroDivisionError:
            rating = 0
        filled_stars = range(1, rating+1)
        unfilled_stars = range(rating+1, 6)

        return {
            "total_reviews": total_reviews,
            "rating": rating,
            "filled_stars": filled_stars,
            "unfilled_stars": unfilled_stars,
        }

    def __str__(self):
        return f"{self.gallery} | {self.title}"
    
    def get_absolute_path(self):
        return reverse("gallery:artwork", args=(self.gallery.owner.username, self.gallery.slug, self.slug))
    


class Comment(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_made")
    content = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    stars = models.IntegerField(blank=False, null=True)

    @property
    def filled_stars(self):
        estrelas = range(1, self.stars+1)

        return estrelas
    
    @property
    def unfilled_stars(self):
        estrelas = range(self.stars+1, 6)

        return estrelas

    def __str__(self):
        return f"{self.user}: {self.content[:25]}"
