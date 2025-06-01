from django.shortcuts import render, redirect
from .models import Profile
from post.models import Post


def profile(request,id):
    users_profile = Profile.objects.get(id = id)
    posts = Post.objects.filter(user = users_profile.user)
    if request.method == 'POST':
        if 'follow' in request.POST:
            current_user_profile= request.user.profile
            action = request.POST['follow']

            if action == 'follow':
                current_user_profile.follows.add(users_profile)
            elif action == 'unfollow':
                current_user_profile.follows.remove(users_profile)

            current_user_profile.save()

    return render(request, 'profile.html',{'profile':users_profile,'posts':posts})


def followers_list(request, user_id):
    # Lista obserwujących
    pass

def following_list(request, user_id):
    # Lista obserwowanych
    pass
