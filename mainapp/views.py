from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image,Profile

@login_required(login_url='login')
def index(request):
    message="Welcome to Instagram"
    images = Image.objects.all()
    return render(request, 'insta/index.html', {'images':images, 'message':message })

def profile(request):
    current_user =request.user
    images = Image.objects.filter(user_id=current_user.id)
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, 'profile.html', {"images": images, "profile": profile})

def save_image(request):
    if request.method=='POST':
       image_name = request.POST['image_name'] 
