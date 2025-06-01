from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self", related_name='followers', blank=True,symmetrical=False)
    bio = models.TextField(blank=True)

    def get_follows_number(self):
        return self.follows.count()

    def get_followers_number(self):
        return self.followers.count()

    def __str__(self):
        return f'{self.user.username} Profile'

