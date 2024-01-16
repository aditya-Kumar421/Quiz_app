from django.urls import path
from .views import  LoginUserView, UserProfileView,RegisterUserView

from knox import views as knox_views

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutAll/', knox_views.LogoutAllView.as_view(), name='logout'), 
]