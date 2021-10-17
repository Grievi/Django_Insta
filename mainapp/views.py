from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image,Profile

@login_required(login_url='login')
def index(request):
    
    images = Image.objects.all()
    return render(request, 'insta/index.html', {'images':images })

def profile(request):
    current_user =request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, 'profile.html', {})
