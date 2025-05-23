from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from post.models import Post
from comment.models import Comment
from .forms import *

def register(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomRegisterForm()
    return render(request,'register.html',{'register_form':form})


@login_required
def my_profile(request):
    username = request.user.username
    posts = Post.objects.filter(user=request.user).order_by('-date_posted')
    return render(request, 'my_profile.html', {'username':username, 'posts':posts})


@login_required
def homepage(request):
    followed_profiles =  request.user.profile.follows.all()
    followed_users = [u.user for u in followed_profiles]
    posts = Post.objects.filter(user__in=followed_users).order_by('-date_posted')
    return render(request, 'homepage.html', {'posts':posts})

def search_user(request):
    if request.method == "POST":
        searched = request.POST['searched']
        users = User.objects.filter(username__contains=searched)
        return render(request,'search_user.html',{'searched':searched,'users':users})
    else:
        return render(request, 'search_user.html', {})