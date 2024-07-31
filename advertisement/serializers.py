from rest_framework.serializers import ModelSerializer
from .models import AdvertisementModel

class AdvertisementGetSerializer(ModelSerializer):
    class Meta:
        model = AdvertisementModel
        fields = "__all__"