from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    message='Hello World'
    return render(request, 'insta/index.html', {'message': message})
