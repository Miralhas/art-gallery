from django import forms

from gallery.models import Artwork, Gallery

class CreateGalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = ["gallery_name", "description", "is_public", "cover_photo"]