from rest_framework.serializers import ModelSerializer
from .models import AccountsModel


class AccountsModelCreateSerializer(ModelSerializer):
    class Meta:
        model = AccountsModel
        fields = ['name','surname','birth','region','phone_number','email','password','image','otp']


class OTPVerifySerializer(ModelSerializer):
    class Meta:
        model = AccountsModel
        fields = ['email','otp']


class LoginSerializer(ModelSerializer):
    class Meta:
        model = AccountsModel
        fields = ['email','password']


class AccountsChangeModelSerializer(ModelSerializer):
    class Meta:
        model = AccountsModel
        fields = ['name', 'surname', 'birth', 'region', 'phone_number', 'image', 'email']

