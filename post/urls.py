from django.urls import path
from .views import createPost, deletePost, editPost, getPostDetails, LikePost

urlpatterns = [
    path('createPost/', createPost, name='createPost'),
    path('delete/<int:post_id>/', deletePost, name = 'deletePost'),
    path('edit/<int:post_id>/', editPost, name = 'editPost'),
    path('details/<int:id>/<slug:slug>', getPostDetails, name = 'post_detail'),
    path('like/<int:id>',LikePost, name = 'like_post')
]