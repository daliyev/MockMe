from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AccountsModel
from .serializers import AccountsModelCreateSerializer, OTPVerifySerializer, LoginSerializer, AccountsChangeModelSerializer
from .utils import hash_password, generate_otp
from django.contrib.auth import authenticate
from django.core.mail import send_mail


class AccountsCreateView(CreateAPIView):
    serializer_class = AccountsModelCreateSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        hashed_password = hash_password(password=password)
        otp = generate_otp()

        if AccountsModel.objects.filter(email=email).exists():
            return Response({"Email already registered"}, status=status.HTTP_400_BAD_REQUEST)

        send_mail(
            "Verification Code",
            f"Your verification code is: {otp} ",
            'TalabaUz <setting.EMAIL_HOST_USER>',
            [email],
            fail_silently=False,
        )

        mutable_data = request.data.copy()

        mutable_data['otp'] = otp
        mutable_data['password'] = hashed_password

        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user = AccountsModel.objects.get(email=email)

        user_info = {
            "id": user.id,
            "name": user.name,
            "surname": user.surname,
            "birth": user.birth,
            "region": user.region,
            "phone_number": user.phone_number,
            "email": user.email,
        }
        return Response(
            user_info,
            status=status.HTTP_200_OK
        )


class OTPVerificationView(GenericAPIView):
    serializer_class = OTPVerifySerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        otp = request.data.get('otp')

        try:
            user = AccountsModel.objects.get(email=email)
        except AccountsModel.DoesNotExist:
            return Response("User not found.", status=status.HTTP_404_NOT_FOUND)

        if not user.otp == otp:
            return Response({'error': 'Provided code is wrong'}, status=status.HTTP_400_BAD_REQUEST)

        user.is_verified = True
        user.otp = ""
        user.save()
        return Response("Your email verified successfully!", status=status.HTTP_200_OK)


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)
        person = AccountsModel.objects.get(email=email)

        if user:
            return Response({
                "id": person.id,
                "name": person.name,
                "surname": person.surname,
                "birth": person.birth,
                "region": person.region,
                "phone_number": person.phone_number,
                "email": person.email,
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)


class ResetPasswordView(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = AccountsModel.objects.get(email=email)
        except AccountsModel.DoesNotExist:
            return Response("You entered wrong email. Please check it. ", status.HTTP_400_BAD_REQUEST)

        otp = generate_otp()
        user.otp = otp
        send_mail(
            "Reset Password Code",
            f"Your password reset code is: {otp} ",
            'TalabaUz <setting.EMAIL_HOST_USER>',
            [email],
            fail_silently=False,
        )
        user.save()
        return Response("Your reset password code has been sent to your email", status.HTTP_200_OK)


class ResetOtpVerify(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')

        try:
            user = AccountsModel.objects.get(email=email)
        except AccountsModel.DoesNotExist:
            return Response("User not found.", status=status.HTTP_404_NOT_FOUND)

        if not user.otp == otp:
            return Response({'error': 'Provided code is wrong'}, status=status.HTTP_400_BAD_REQUEST)

        user.password = ""
        user.otp = ""
        user.save()
        return Response("Send reset password ", status=status.HTTP_200_OK)


class SetNewPasswordView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = AccountsModel.objects.get(email=email)
        except AccountsModel.DoesNotExist:
            return Response("You entered wrong email. Please check it. ", status.HTTP_400_BAD_REQUEST)

        if user.password != "":
            return Response("Something went wrong. Please check entered reset code verified first",
                            status.HTTP_400_BAD_REQUEST)

        user.password = hash_password(password)
        user.save()
        return Response("Your password reseted!", status.HTTP_200_OK)


class AccountRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = AccountsModel.objects.all()
    serializer_class = AccountsChangeModelSerializer
    lookup_field = 'id'