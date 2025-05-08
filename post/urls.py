from django.urls import path, include
from .views import createPost, deletePost

urlpatterns = [
    path('createPost/', createPost, name='createPost'),
    path('delete/<int:post_id>/', deletePost, name = 'deletePost'),
]