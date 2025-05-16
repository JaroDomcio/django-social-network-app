from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(User, related_name='followers', blank=True,symmetrical=False)
    bio = models.TextField(blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'