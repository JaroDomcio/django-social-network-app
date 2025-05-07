from django.urls import path, include
from .views import createPost

urlpatterns = [
    path('createPost/', createPost, name='createPost'),

]