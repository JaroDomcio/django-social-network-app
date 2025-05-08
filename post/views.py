from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from post.forms import PostForm
from .models import Post

@login_required()
def createPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            redirect('home')
    else:
        form = PostForm()
    return render(request,'create_post.html',{'form':form})

@login_required
def deletePost(request,post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    post.delete()
    return redirect('home')
