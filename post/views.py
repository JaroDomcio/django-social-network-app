from django.shortcuts import render, redirect

from post.forms import PostForm


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
