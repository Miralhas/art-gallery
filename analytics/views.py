from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView, View

from accounts.models import User
from analytics.utils import color_generator, single_color_bar_vs_all_others
from gallery.models import Artwork, Gallery

# Create your views here.

class IndexView(TemplateView):
    template_name = "analytics/index.html"


def get_most_viewed_galleries(request):
    galleries = Gallery.objects.order_by("views")
    colors = color_generator(len(galleries))
    # returns a queryset ordered from most to least viewed gallery.

    data = {
        "labels": [gallery.gallery_name for gallery in galleries], # x axis
        "datasets": [{
            "label": "Most Viewed Galleries", # label to each value
            "data": [gallery.views for gallery in galleries], # values in y axis
            "backgroundColor": colors[0],
            "borderColor": colors[1],
            "borderWidth": 0.2
        }]
    }
    return JsonResponse(data)


def get_most_rated_artworks(request):
    queryset = Artwork.objects.filter()
    artworks = sorted(queryset, key=lambda artwork: artwork.review_status["rating"])
    colors = color_generator(len(artworks))

    data = {
        "labels": [artwork.title for artwork in artworks],
        "datasets": [{
            "label": "Most Rated Artworks",
            "data": [artwork.review_status["rating"] for artwork in artworks],
            "backgroundColor": colors[0],
            "borderColor": colors[1],
            "borderWidth": 0.2
        }]
    }
    return JsonResponse(data)


def get_most_viewed_user_profiles(request):
    users = User.objects.order_by("views")
    colors = color_generator(len(users))

    data = {
        'labels': [user.username for user in users],
        'datasets': [{
            'label': 'Profile Views',
            'data': [user.views for user in users],
            "backgroundColor": colors[0],
            "borderColor": colors[1],
            "borderWidth": 0.2
        }]
    }

    return JsonResponse(data)


def get_gallery_analytics(request, slug):
    galleries_queryset = Gallery.objects.filter(slug=slug)
    if not galleries_queryset.exists():
        return JsonResponse({"message": "Gallery provided does not exist!"}, status=404)
    
    gallery = galleries_queryset.first()
    artworks = gallery.artworks.order_by("views")
    colors = color_generator(len(artworks))

    data = {
        "labels": [artwork.title for artwork in artworks],
        "datasets": [{
            "label": f"Most Viewed Artworks in {gallery.gallery_name}",
            "data": [artwork.views for artwork in artworks],
            "backgroundColor": colors[0],
            "borderColor": colors[1],
            "borderWidth": 0.2
        }]
    }
    return JsonResponse(data)


def get_artwork_analytics_vs_all(request, slug):
    artworks = Artwork.objects.order_by("views")
    try:
        artwork = Artwork.objects.get(slug=slug)
    except Artwork.DoesNotExist:
        return JsonResponse({"message": "Artwork provided does not exist!"}, status=404)
    
    artwork_index = Artwork.objects.order_by("views").filter(views__lt=artwork.views).count()
    colors = single_color_bar_vs_all_others(artwork_index, len(artworks))

    data = {
        "labels": [artwork.title for artwork in artworks],
        "datasets": [{
            "label": f"{artwork.title} vs All Artworks",
            "data": [artwork.views for artwork in artworks],
            "backgroundColor": colors[0],
            "borderColor": colors[1],
            "borderWidth": 0.2
        }]
    }
    return JsonResponse(data)