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

def like_image(request, id):
    likes = Likes.objects.filter(image_id=id).first()
    if Likes.objects.filter(image_id=id, user_id=request.user.id).exists():
        # This will unlike
        likes.delete()
        image = Image.objects.get(id=id)
        if image.like_count == 0:
            image.like_count = 0
            image.save()
        else:
            image.like_count -= 1
            image.save()
        return redirect('home')
    else:
        likes = Likes(image_id=id, user_id=request.user.id)
        likes.save()
        image = Image.objects.get(id=id)
        image.like_count = image.like_count + 1
        image.save()
        return redirect('home')

def single_image(request, id):
    image = Image.objects.get(id=id)
    related_images = Image.objects.filter(
        user_id=image.user_id).order_by('-image_date')
    title = image.image_name
    if Image.objects.filter(id=id).exists():
        comments = Comment.objects.filter(image_id=id)
        return render(request, 'picture.html', {'image': image, 'comments': comments, 'images': related_images, 'title': title})
    else:
        return redirect('home')

def save_comment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        image_id = request.POST['image_id']
        image = Image.objects.get(id=image_id)
        user = request.user
        comment = Comment(comment=comment, image_id=image_id, user_id=user.id)
        comment.save_comment()
        image.comment_count = image.comment_count + 1
        image.save()
        return redirect('/picture/' + str(image_id))
    else:
        return redirect('home')