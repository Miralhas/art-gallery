from django.urls import path
from gallery import views

app_name = "gallery"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("create-gallery", views.CreateGalleryView.as_view(), name="create_gallery"),
    path("create-artwork/<str:username>/<slug:slug>", views.CreateArtworkView.as_view(), name="create_artwork"),
    path("galleries/<str:username>/<slug:slug>", views.UserGallerieView.as_view(), name="gallery"),
]