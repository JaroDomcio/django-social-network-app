from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length= 250)
    # slug = models.SlugField(max_length= 250)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post_detail', kwargs={'slug': self.slug})
