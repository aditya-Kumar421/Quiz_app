from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from .serializers import UserSerializer
from .models import OTPValidation

# from knox.auth import AuthToken
from datetime import timedelta


class MyThrottle(UserRateThrottle):
    scope = 'my_scope'
    rate = '10/day' 

class GenerateOTPView(APIView):
    throttle_classes = [MyThrottle]
    def post(self, request):
        email = request.data.get('email')
        user_name = request.data.get('username')

        if not email or not user_name:
            return Response({'error': 'Email and username are required'}, status=status.HTTP_400_BAD_REQUEST)

        otp = get_random_string(length=6, allowed_chars='123456789')
        expired_at = timezone.now() + timedelta(seconds=90)

        try:
            OTPValidation.objects.create(user_name = user_name, user_email=email, otp=otp, expired_at=expired_at)
        except IntegrityError:
                return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        subject = 'OTP for quiz registration'
        message = f'Your OTP is: {otp}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f'Failed to send OTP: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ResendOTP(APIView):
    throttle_classes = [MyThrottle]
    def post(self, request):
        email = request.data.get('email')
        user_name = request.data.get('username')

        try:
            otp_record = OTPValidation.objects.get(user_name = user_name, user_email=email)
        except OTPValidation.DoesNotExist:
            return Response({"error": "OTP record not found"}, status=status.HTTP_404_NOT_FOUND)

        new_otp = get_random_string(length=6, allowed_chars='123456789')
        otp_record.expired_at = timezone.now() + timedelta(seconds=90)
        otp_record.otp = new_otp
        otp_record.save()

        subject = 'OTP for registration'
        message = f'Your OTP is: {new_otp}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f'Failed to send OTP: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ValidateEmailView(APIView):
    throttle_classes = [MyThrottle]
    def post(self, request):
        otp = request.data.get('otp')
        if not otp:
            return Response({'error': 'OTP is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            otp_obj = OTPValidation.objects.get(otp=otp)
        except OTPValidation.DoesNotExist:
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

        if otp_obj.is_expired():
            # otp_obj.delete()
            return Response({'error': 'OTP expired'}, status=status.HTTP_400_BAD_REQUEST)
        
        email = otp_obj.user_email
        user_name = otp_obj.user_name

        otp_obj.delete()

        user_data = {'username':user_name, 'email': email}
        serializer = UserSerializer(data=user_data)

        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response({
                'user_info': {
                    'username': user.username, 
                    'email': user.email
                },
                'token': token
            })
        
        try:
            user_detail = User.objects.get(username=user_name, email=email) 
        except User.DoesNotExist:
            return Response({"error": "OTP record not found"}, status=status.HTTP_404_NOT_FOUND)
        
        user_detail.delete()

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"detail": "Logged out successfully"})