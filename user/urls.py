from django.urls import path
from .views import register,my_profile, search_user, homepage, settings
from django.contrib.auth.views import LoginView,LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('settings/', settings, name='settings'),
    path('my-profile/' , my_profile , name='my_profile'),
    path('homepage/', homepage, name='homepage'),
    path('search_user/',search_user,name='search_user'),
]