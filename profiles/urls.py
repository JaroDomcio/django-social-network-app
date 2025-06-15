from django.urls import path
from .views import profile, followers_list, following_list

urlpatterns = [
    path('profile/<int:id>',profile, name='profile'),
    path('followers/<int:id>/',followers_list, name='followers_list'),
    path('following/<int:id>/',following_list,name='following_list'),
]