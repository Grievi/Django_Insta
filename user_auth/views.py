from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    message='Instagram'
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user =authenticate(username=username, password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request, (f"welcome to Instagram"))
        else:
            messages.success(request,("Something went wrong"))

            return render(request, 'authentication/login.html')
    else:
        return render(request, 'authentication/login.html', {})
