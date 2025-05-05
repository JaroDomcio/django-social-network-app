from django.urls import path, include
from .views import register,home

urlpatterns = [
    path('register/', register, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('home/' , home , name='home'),
]