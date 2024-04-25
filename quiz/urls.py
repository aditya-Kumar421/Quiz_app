from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('http://127.0.0.1:8000//', admin.site.urls),
    path('api/', include('question.urls')),
    path('auth/', include('user.urls')),
]