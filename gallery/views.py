import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import F
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DeleteView
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView

from accounts.models import User
from gallery.forms import CreateArtworkForm, CreateCommentForm, CreateGalleryForm
from gallery.models import Artwork, Comment, Gallery
from gallery.utils import unique_slugify

# Create your views here.

class IndexView(TemplateView):
    template_name = "gallery/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["galleries"] = Gallery.objects.all().order_by("-views")[:3]

        return context


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


class DeleteGalleryView(LoginRequiredMixin, DeleteView):
    model = Gallery
    success_url = "/"


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
    

class DeleteArtworkView(LoginRequiredMixin, DeleteView):
    model = Artwork

    def get_success_url(self):
        gallery = Gallery.objects.get(artworks__slug="athena")
        return gallery.get_absolute_path()


class UserGallerieView(DetailView):
    model = Gallery
    template_name = "gallery/user_gallery.html"
    context_object_name = "gallery"
    form_class = CreateArtworkForm

    def get_context_data(self, **kwargs):
        gallery = Gallery.objects.get(slug=self.kwargs["slug"])
        Gallery.objects.filter(slug=self.kwargs["slug"]).update(views=F("views") + 1)

        artworks = gallery.artworks.all().order_by("-views")
        paginator = Paginator(artworks, 6)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = super().get_context_data(**kwargs)
        context["artworks"] = artworks
        context["form"] = self.form_class()
        context["page_obj"] = page_obj
        return context


class ArtworkPageView(DetailView):
    model = Artwork
    template_name = "gallery/artwork.html"
    context_object_name = "artwork"
    form_class = CreateCommentForm

    def get_context_data(self, **kwargs):
        Artwork.objects.filter(id=kwargs["object"].id).update(views=F("views") + 1)
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class()
        context["comments"] = Comment.objects.filter(artwork=kwargs["object"])
        context["stars"] = range(1, 6)
        return context
    
    def post(self, request, **kwargs):
        artwork = Artwork.objects.get(slug=kwargs["slug"])
        form = self.form_class(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.artwork = artwork
            new_comment.user = request.user
            new_comment.stars = request.POST.get("starValue")
            new_comment.save()

        return HttpResponseRedirect(artwork.get_absolute_path())
    

def edit_artwork_view(request, slug):
    if request.method != "PUT":
        return JsonResponse({"error": "PUT request required."}, status=400)
    
    data = json.loads(request.body)
    new_artwork_title = data["newArtworkTitle"]
    new_artwork_description = data["newArtworkDescription"]

    try:
        artwork_owner = User.objects.get(email=data["artworkOwner"])
    except User.DoesNotExist:
        return JsonResponse({"message": "User provided does not exist!"}, status=404)
    
    try:
        artwork = Artwork.objects.get(slug=data["artworkSlug"])
    except Artwork.DoesNotExist:
        return JsonResponse({"message": "Artwork provided does not exist!"}, status=404)
    
    if artwork.gallery.owner != artwork_owner:
        return JsonResponse({"message": "User provided is not the artwork owner!"}, status=403)

    newUrl = data["path"]
    slug = artwork.slug

    if artwork.title != new_artwork_title:
        slug = unique_slugify(Artwork, string_to_slugify=new_artwork_title, model=Artwork)
        newUrl = f"/galleries/{artwork.gallery.owner.username}/{artwork.gallery.slug}/artworks/{slug}"

    artwork.title = new_artwork_title
    artwork.description = new_artwork_description
    artwork.slug = slug
    artwork.save()
    return JsonResponse({"message": "Ok", "newUrl": newUrl, "newSlug": slug}, status=200)


def edit_gallery_view(request, slug):
    if request.method != "PUT":
        return JsonResponse({"error": "PUT request required."}, status=400)
    
    data = json.loads(request.body)
    new_gallery_name = data["newGalleryName"]
    new_gallery_description = data["newGalleryDescription"]

    try:
        gallery_owner = User.objects.get(email=data["galleryOwner"])
    except User.DoesNotExist:
        return JsonResponse({"message": "User provided does not exist!"}, status=404)
    
    try:
        gallery = Gallery.objects.get(slug=data["gallerySlug"])
    except Gallery.DoesNotExist:
        return JsonResponse({"message": "Gallery provided does not exist!"}, status=404)
    
    if gallery.owner != gallery_owner:
        return JsonResponse({"message": "User provided is not the gallery owner!"}, status=403)

    newUrl = data["path"]
    slug = gallery.slug

    if gallery.gallery_name != new_gallery_name:
        slug = unique_slugify(Gallery, string_to_slugify=new_gallery_name, model=Gallery)
        newUrl = f"/galleries/{gallery.owner.username}/{slug}/"

    gallery.gallery_name = new_gallery_name
    gallery.description = new_gallery_description
    gallery.slug = slug
    gallery.save()
    return JsonResponse({"message": "Ok", "newUrl": newUrl, "newSlug": slug}, status=200)

