from rest_framework.generics import GenericAPIView
from .models import ResultsModel 
from .serializers import LastResultSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response 
from rest_framework import status


class LastResultView(GenericAPIView):
    serializer_class = LastResultSerializer

    def get(self, request, user_id):
        try:
            queryset = ResultsModel.objects.filter(user_id=user_id).last()
            if queryset is None:
                raise ResultsModel.DoesNotExist
        except ResultsModel.DoesNotExist:
            return Response("User Not Found", status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


