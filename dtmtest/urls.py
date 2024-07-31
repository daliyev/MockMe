from django.urls import path
from .views import TestCollectionListView, TestColletionDetailView,  DtmTestsView
urlpatterns = [
    path('testcollections/',TestCollectionListView.as_view()),
    path('testcollection/<str:code>/',TestColletionDetailView.as_view()),
    path('dtmteststart/<str:code>/', DtmTestsView.as_view()),
]