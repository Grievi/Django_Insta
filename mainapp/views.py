from django.shortcuts import render

def index(request):
    message='Hello World'
    return render(request, 'insta/index.html', {'message': message})
