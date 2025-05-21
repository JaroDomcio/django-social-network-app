from django.urls import path
from .views import register,my_profile, search_user, homepage
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('my_profile/' , my_profile , name='my_profile'),
    path('homepage/', homepage, name='homepage'),
    path('search_user/',search_user,name='search_user'),
]