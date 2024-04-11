
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User

from .serializers import MailSerializer, UserSerializer
from .models import Mail, OTPValidation
from knox.auth import AuthToken

class GenerateOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        otp = get_random_string(length=6, allowed_chars='123456789')
        OTPValidation.objects.create(user_email=email, otp=otp)

        subject = 'OTP for registration'
        message = f'Your OTP is: {otp}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f'Failed to send OTP: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ValidateEmailView(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')
        if not email or not otp:
            return Response({'error': 'Email and OTP are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            otp_obj = OTPValidation.objects.get(user_email = email, otp=otp)
        except OTPValidation.DoesNotExist:
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        # print(otp_obj)
        otp_obj.delete()

        user_data = {'email': email}
        serializer = MailSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        user_detail = Mail.objects.get(email = email) 
        user_detail.delete()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RegisterUserView(APIView):
    def post(self, request):
            serializer = UserSerializer(data=request.data)
            try:
                email = Mail.objects.get(email =  request.data.get('email'))
            except Mail.DoesNotExist:
                return Response({'error': 'Email is not verified'}, status=status.HTTP_400_BAD_REQUEST)
            # print(email)
            if email:
                if serializer.is_valid():
                    user = serializer.save()
                    _, token = AuthToken.objects.create(user)
                    return Response({'user_info':{
                                        'username':user.username, 
                                        'email':user.email
                                        },
                            'token': token})
                return Response({'error':'check your credentials.'}, status=400)
            return Response({'error':'enter email.'}, status=400)
