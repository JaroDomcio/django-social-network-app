
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length= 250)
    likes = models.ManyToManyField(User, related_name='Post_likes')
    slug = models.SlugField(null = False,default='')
    content = models.TextField(null=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'post_images/',blank = True, null= True)

    class Meta:
        unique_together = ('user', 'slug')


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'id':self.id, 'slug': self.slug})
