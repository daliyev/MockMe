from .models import AccountsModel
from django.contrib.auth.backends import BaseBackend
from .utils import verify_password

class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = AccountsModel.objects.get(email=email)
            if verify_password(password,user.password):
                return user
        except AccountsModel.DoesNotExist:
            return None