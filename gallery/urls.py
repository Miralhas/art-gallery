from django.urls import path
from gallery import views

app_name = "gallery"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("create-gallery", views.CreateGalleryView.as_view(), name="create_gallery"),
    path("delete-gallery/<slug:slug>", views.DeleteGalleryView.as_view(), name="delete_gallery"),
    path("create-artwork/<str:username>/<slug:slug>", views.CreateArtworkView.as_view(), name="create_artwork"),
    path("delete-artwork/<str:username>/<slug:slug>", views.DeleteArtworkView.as_view(), name="delete_artwork"),
    path("galleries/", views.GalleriesListView.as_view(), name="galleries"),
    path("artworks/", views.ArtworkListView.as_view(), name="artworks"),
    path("galleries/<str:username>/<slug:slug>/", views.UserGallerieView.as_view(), name="gallery"),
    path("galleries/<str:username>/<slug:gallery_slug>/artworks/<slug:slug>", views.ArtworkPageView.as_view(), name="artwork"),

    path("api/edit-galleries/<slug:slug>", views.edit_gallery_view, name="edit_gallery"),
    path("api/edit-artworks/<slug:slug>", views.edit_artwork_view, name="edit_artwork"),
]