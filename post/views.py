from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from post.forms import PostForm, EditPostForm
from .models import Post
from comment.models import Comment

@login_required()
def createPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('my_profile')
    else:
        form = PostForm()
    return render(request,'create_post.html',{'form':form})

@login_required
def deletePost(request,post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    post.delete()
    return redirect('my_profile')

@login_required
def editPost(request,post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)

    if request.method == 'POST':
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid():
            form = form.save()
            return redirect('my_profile')

    else:
        form = EditPostForm(instance=post)

    return render(request,'edit_post.html',{'form':form})

def getPostDetails(request,id,slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    comments= Comment.objects.filter(post=post).all()
    return render(request,'post_detail.html',{'post':post,'comments':comments})

def LikePost(request,id):
    post = Post.objects.get(id=id)

    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect(request.META.get('HTTP_REFERER', '/'))