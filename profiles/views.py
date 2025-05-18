from django.shortcuts import render
from .models import Profile
from post.models import Post


def profile(request,id):
    users_profile = Profile.objects.get(id = id)
    posts = Post.objects.filter(user = users_profile.user)
    return render(request, 'profile.html',{'profile':users_profile,'posts':posts})
