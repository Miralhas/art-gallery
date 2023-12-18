from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView

from accounts.models import User
from gallery.forms import (CreateArtworkForm, CreateCommentForm,
                           CreateGalleryForm)
from gallery.models import Artwork, Gallery, Comment
from gallery.utils import unique_slugify

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
        new_gallery.slug = unique_slugify(self, string_to_slugify=new_gallery.gallery_name, model=self.model)
        # cover_photo =
        new_gallery.save()
        self.success_url = reverse("gallery:gallery", args=(new_gallery.owner.username, new_gallery.slug))
        
        return super().form_valid(form)


class CreateArtworkView(LoginRequiredMixin, View):
    model = Artwork
    form_class = CreateArtworkForm

    def post(self, request, **kwargs):
        user = User.objects.get(username=kwargs["username"])
        if user != request.user:
            return HttpResponseRedirect(reverse("gallery:index"))
        gallery = Gallery.objects.get(slug=kwargs["slug"])

        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            new_artwork = form.save(commit=False)
            new_artwork.gallery = gallery
            new_artwork.slug = unique_slugify(self, string_to_slugify=new_artwork.title, model=self.model)
            new_artwork.save()
        else:
            print("invalid")

        return HttpResponseRedirect(reverse("gallery:gallery", args=(gallery.owner.username, gallery.slug)))



class UserGallerieView(DetailView):
    model = Gallery
    template_name = "gallery/user_gallery.html"
    context_object_name = "gallery"
    form_class = CreateArtworkForm

    def get_context_data(self, **kwargs):
        gallery = Gallery.objects.get(slug=self.kwargs["slug"])
        context = super().get_context_data(**kwargs)
        context["artworks"] = gallery.artworks.all()
        context["form"] = self.form_class()
        return context


class ArtworkPageView(LoginRequiredMixin, DetailView):
    model = Artwork
    template_name = "gallery/artwork.html"
    context_object_name = "artwork"
    form_class = CreateCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class()
        context["comments"] = Comment.objects.filter(artwork=kwargs["object"])
        return context
    
    def post(self, request, **kwargs):
        artwork = Artwork.objects.get(slug=kwargs["slug"])
        user = User.objects.get(username=kwargs["username"])
        form = self.form_class(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.artwork = artwork
            new_comment.user = user
            new_comment.save()

        return HttpResponseRedirect(artwork.get_absolute_path())
    

    