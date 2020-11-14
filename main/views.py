from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *
# Create your views here.

def homepage(request):
    return render(request, 'home.html')

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect.')
            
            
    context = {}
    return render(request, 'login.html', context)

def signupPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('first_name')
            messages.success(request, 'Your account has been created, ' +  name)

            return redirect('login')

    context = {'form':form}
    return render(request, 'signup.html', context)