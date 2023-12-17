from django.contrib import admin

from gallery.models import Artwork, Gallery

# Register your models here.

admin.site.register(Gallery)
admin.site.register(Artwork)
