from django.urls import path, include
from .views import DtmTestListView, DtmTestDetailView, StudentTestResultListView, StudentTestResult, DtmDirectionListView

urlpatterns = [
    path('directions/', DtmDirectionListView.as_view(), name='directions'),
    path('tests/<int:direction_code>', DtmTestListView.as_view(), name='dtmtest'),
    path('tests/<int:pk>/', DtmTestDetailView.as_view(), name='dtmtestdetail'),
    path('result/<int:user_id>', StudentTestResultListView.as_view(), name='dtmtestresult'),
    path('result/', StudentTestResult.as_view(), name='dtmtestresult'),
]