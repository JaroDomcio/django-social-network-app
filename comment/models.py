from django.contrib.auth.models import User
from django.db import models

from post.models import Post


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    is_edited = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.content

