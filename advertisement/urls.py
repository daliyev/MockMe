from django.urls import path
from .views import AdvertisementAllView
urlpatterns = [
    path("get/",AdvertisementAllView.as_view()),
]