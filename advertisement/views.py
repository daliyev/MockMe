from rest_framework import generics
from .models import AdvertisementModel
from .serializers import AdvertisementGetSerializer

class AdvertisementAllView(generics.ListAPIView):
    queryset = AdvertisementModel.objects.all()
    serializer_class = AdvertisementGetSerializer
