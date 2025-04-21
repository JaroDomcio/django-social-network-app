from django.shortcuts import render,redirect
from .forms import *

def register(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = CustomRegisterForm()
    return render(request,'register.html',{'register_form':form})
