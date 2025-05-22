from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from post.models import Post


def CreateComment(request,id):
    post = get_object_or_404(Post,id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail',id = id, slug = post.slug)
    else:
        form = CommentForm()
    return render(request,'create_comment.html',{'form':form})