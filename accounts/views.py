from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect



def register(request):
    if request.method == 'POST':
       # Get form values
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       password2 = request.POST['password2']

        # Check if passwords match
       if password1 == password2:
            return
       else:
             messages.error(request, 'Passwrods do not match')
             return redirect('register')
    else:
        return render(request, 'accounts/register.html'  )

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=username, password=password)
        if username is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html'  )

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html'  )


