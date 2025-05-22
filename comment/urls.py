from django.urls import path
from .views import CreateComment

urlpatterns = [
    path('post/<int:id>/comment', CreateComment, name='CreateComment')
]