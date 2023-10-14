from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate, login


def home(request):
    return render(request,'home.html')

def login_page(request):
    return render(request,'login.html')

def login_action(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if not username or not password:
            messages.error(request, 'All fields must be filled in.')
            return redirect('login_page')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Authentication successful; log the user in
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login_page')
    else:
        messages.error(request, 'Invalid request method')
        return redirect('login_page')

def signup_page(request):
    return render(request,'signup.html')
    
def signup_action(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if not username or not email or not password:
            messages.error(request, 'All fields must be filled in.')
            return redirect('signup_page')
        
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('signup_page')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            auth.login(request, user)
            return redirect('signup_page')
    else:
        messages.info(request,'Invalid')
        return redirect('signup_page')
    
def logout(request):
    auth.logout(request)
    return redirect('/')
    
