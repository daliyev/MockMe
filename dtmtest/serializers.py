from rest_framework import serializers
from .models import TestCollectionModel, TestModel , DTMTestModel

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'

class TestCollectionModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCollectionModel
        fields = ['id','code','subject','is_free','tests']

class TestCollectionModelDetailSerializer(serializers.ModelSerializer):
    tests = TestSerializer(many = True)
    class Meta:
        model = TestCollectionModel
        fields = ['id','code','subject','is_free','tests']

class DTMModelSerializer(serializers.ModelSerializer):
    testcollection = TestCollectionModelDetailSerializer(many = True)
    class Meta:
        model = DTMTestModel
        fields = ['id','code','is_started','testcollection']


class UploadQuestionsFile(serializers.Serializer):
    file = serializers.FileField()
