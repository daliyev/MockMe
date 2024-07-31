from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from .models import TestCollectionModel, DTMTestModel ,TestModel
from rest_framework.decorators import api_view
from .serializers import (
    TestCollectionModelListSerializer,
    TestCollectionModelDetailSerializer,
    DTMModelSerializer,
    TestSerializer)
from django.utils import timezone
import random


class TestCollectionListView(generics.ListAPIView):
    serializer_class = TestCollectionModelListSerializer
    
    def get_queryset(self, *args, **kwargs):
        subject = self.kwargs.get('subject')
        test_collections = list(TestCollectionModel.objects.filter(is_free=True, subject=subject))
        random.shuffle(test_collections)
        return test_collections[:2]


class TestColletionDetailView(generics.RetrieveAPIView):
    serializer_class = TestCollectionModelDetailSerializer
    lookup_url_kwarg = 'code'  

    def get_queryset(self):
        code = self.kwargs.get('code')
        queryset = TestCollectionModel.objects.filter(code = code)
        return queryset
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()  
        
        if obj is None:
            raise NotFound("No matching tests found.")
        
        return obj
    

class DtmTestsView(generics.RetrieveAPIView):
    serializer_class = DTMModelSerializer
    lookup_url_kwarg = 'code'

    def get_queryset(self):
        code = self.kwargs.get('code')
        queryset = DTMTestModel.objects.filter(code = code)
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()

        if obj is None:
            raise NotFound("No matching tests found.")
        elif obj.is_started == False:
            raise NotFound("The test haven't been started yet.")

        return obj


class TestListView(generics.ListAPIView):
    serializer_class = TestSerializer

    def get_queryset(self):
        subject = self.kwargs['subject']
        return TestModel.objects.filter(subject=subject)[:30]


class TestDetailView(generics.RetrieveAPIView):
    serializer_class = TestCollectionModelDetailSerializer
    

# @api_view("POST")
# def upload_file(request):
#     file = request.FILES.get['file']
#     if not file:
#         return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)
#
#     content = file.read().decode('utf-8')
#     questions = content.split('+++++')
#
#     for question in questions:
#         if not question.strip():
#             continue
#         lines = question.strip.split('\n')
#         question_text = lines[0].stripe()
#         anserA = question_text[1]
#         anserB = question_text[2]
#         anserC = question_text[3]
#         anserD = question_text[4]
#         answer_correct = anserA
#
#
#


