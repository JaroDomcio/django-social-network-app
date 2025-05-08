from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from post.models import Post
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
def home(request):
    username = request.user.username
    posts = Post.objects.filter(user=request.user).order_by('-date_posted')
    return render(request,'home.html',{'username':username,'posts':posts})

