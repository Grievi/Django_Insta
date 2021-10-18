from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *

@login_required(login_url='login')
def index(request):
    message="Welcome to Instagram"
    images = Image.objects.all()
    return render(request, 'insta/index.html', {'images':images, 'message':message })

@login_required(login_url='login')
def profile(request):
    current_user =request.user
    images = Image.objects.filter(user_id=current_user.id)
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, 'profile.html', {"images": images, "profile": profile})

@login_required(login_url='login')
def save_image(request):
    if request.method == 'POST':
        image_name = request.POST['image_name']
        image_caption = request.POST['image_caption']
        image_file = request.FILES['image_file']
        image_url = image_file['url']
        image_public_id = image_file['public_id']
        image = Image(image_name=image_name, image_caption=image_caption, image=image_url,
                      profile_id=request.POST['user_id'], user_id=request.POST['user_id'])
        image.save_image()

        return redirect('/profile', {'success': 'Image Uploaded Successfully'})
    else:
        return render(request, 'profile.html', {'message':'Upload image!'})





@login_required(login_url='login')
def search_images(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search').lower()
        images = Image.search_by_image_name(search_term)
        message = f'{search_term}'
        title = message

        return render(request, 'search.html', {'success': message, 'images': images})
    else:
        message = 'You havent searched for any term'
        return render(request, 'search.html', {'danger': message})