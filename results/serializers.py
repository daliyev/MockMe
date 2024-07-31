from rest_framework.serializers import ModelSerializer
from .models import ResultsModel
from dtmtest.models import TestCollectionModel

class TestSubjectSerializer(ModelSerializer):
    class Meta:
        model = TestCollectionModel
        fields = ["subject"]
class LastResultSerializer(ModelSerializer):
    test_id = TestSubjectSerializer()
    class Meta:
        model = ResultsModel
        fields = ["id","user_id","point","date","test_id"]
