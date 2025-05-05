from django.shortcuts import render,redirect
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


def home(request):
    return render(request,'home.html')