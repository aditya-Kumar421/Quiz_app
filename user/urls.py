from django.urls import path
from .views import GenerateOTPView, ValidateEmailView, ResendOTP, LogoutView
# from knox import views as knox_views

urlpatterns = [
    path('validate/', ValidateEmailView.as_view(), name='register'),
    path('resend/', ResendOTP.as_view()),
    path('otp/', GenerateOTPView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
]