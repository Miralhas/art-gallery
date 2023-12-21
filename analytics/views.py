from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView, View

from accounts.models import User
from gallery.models import Artwork, Gallery

# Create your views here.

class IndexView(TemplateView):
    template_name = "analytics/index.html"


def get_most_viewed_galleries(request):
    galleries = Gallery.objects.order_by("views")
    # returns a queryset ordered from most to least viewed gallery.

    data = {
        "labels": [gallery.gallery_name for gallery in galleries], # x axis
        "datasets": [{
            "label": "Gallery Views", # label to each value
            "data": [gallery.views for gallery in galleries], # values in y axis
            "backgroundColor": [],
            "borderColor": "#FFFFFF",
            "borderWidth": 0.2
        }]
    }
    return JsonResponse(data)