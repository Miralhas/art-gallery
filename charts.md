# Charts

1. Chart displaying most Viewed Galleries
2. Chart displaying most rated Artworks
3. Chart displaying most Viewed Users

***
## Galleries
``` python
from django.http import JsonResponse

def get_most_viewed_galleries(request):
    galleries = Gallery.objects.order_by("-views")
    # returns a queryset ordered from most to least viewed gallery.

    data = {
        "labels": [gallery.gallery_name for gallery in galleries],
        "datasets": [{
            "label": "Gallery Views",
            "data": [galery.views for gallery in galleries]
        }]
    }
    return JsonResponse(data)
```

***
## Artworks
```python
from django.http import JsonResponse

def get_most_rated_artworks(request):
    queryset = Artworks.objects.all()
    artworks = sorted(queryset, key=lambda artwork: artwork.review_status["rating"], reverse=True)
```

***
## Users
```python
from django.http import JsonResponse

def get_most_viewed_profiles(request):
    # Get the top 5 users with the most views
    users = User.objects.order_by("-views")[:5]
    # Prepare the data for the response
    data = {
        'labels': [user.username for user in users],
        'datasets': [{
            'label': 'Profile Views',
            'data': [user.views for user in users],
        }]
    }
    return JsonResponse(data)
```