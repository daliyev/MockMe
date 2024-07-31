from django.urls import path
from .views import( 
    AccountsCreateView,
    LoginAPIView,
    OTPVerificationView,
    ResetPasswordView,
    ResetOtpVerify,
    SetNewPasswordView,
    AccountRetrieveUpdateView
)

urlpatterns = [
    path('signup/',AccountsCreateView.as_view()),
    path('signup/otpverification/',OTPVerificationView.as_view()),
    path('login/',LoginAPIView.as_view()),
    path('resetpass/sendotp/',ResetPasswordView.as_view()),
    path('resetpass/otpverification/',ResetOtpVerify.as_view()),
    path('setnewpass/',SetNewPasswordView.as_view()),
    path('update/<int:id>/', AccountRetrieveUpdateView.as_view(), name='account_update'),

]
