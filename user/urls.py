from django.urls import path
from .views import  RegisterUserView, GenerateOTPView, ValidateEmailView
from knox import views as knox_views

urlpatterns = [
    path('validate/', ValidateEmailView.as_view(), name='register'),
    path('otp/', GenerateOTPView.as_view()),
    path('register/', RegisterUserView.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
]