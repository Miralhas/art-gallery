from django.urls import path

from analytics import views


app_name = "analytics"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("api/most_viewed_galleries", views.get_most_viewed_galleries, name="most_viewed_galleries"),
]
