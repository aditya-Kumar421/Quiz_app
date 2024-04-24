from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('nimbusquizdatabase/', admin.site.urls),
    path('api/', include('question.urls')),
    path('auth/', include('user.urls')),
]