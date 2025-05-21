from django.urls import path
from .views import profile

urlpatterns = [
    path('profile/<int:id>',profile, name='profile')
]