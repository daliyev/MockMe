from django.urls import path
from .views import LastResultView


urlpatterns = [
    path('lastsolvedtestget/<int:user_id>/', LastResultView.as_view()),
    # path('uploadfile/',)
]
