from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.utils.text import slugify
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from gallery.forms import CreateGalleryForm
from gallery.models import Artwork, Gallery

# Create your views here.

class IndexView(TemplateView):
    template_name = "gallery/index.html"


class CreateGalleryView(LoginRequiredMixin, CreateView):
    model = Gallery
    template_name = "gallery/create_gallery.html"
    form_class = CreateGalleryForm

    def form_valid(self, form):
        new_gallery = form.save(commit=False)
        new_gallery.owner = self.request.user
        new_gallery.slug = slugify(new_gallery.gallery_name)
        # cover_photo =
        new_gallery.save()
        self.success_url = reverse("gallery:gallery", args=(new_gallery.owner.username, new_gallery.slug))
        
        return super().form_valid(form)


class UserGallerieView(DetailView):
    model = Gallery
    template_name = "gallery/user_gallery.html"
    context_object_name = "gallery"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["range"] = range(0, 5)
        return context