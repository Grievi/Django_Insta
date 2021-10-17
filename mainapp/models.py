from django.db import models
import datetime as dt
from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    username=models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    bio = models.CharField(max_length=500)
    profile_photo = models.ImageField(upload_to='media/', default='default.png')

    def __str__(self):
        return self.user.username 

    def save_profile(self):
        self.save()

    def update_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Image(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='images')
    image= models.ImageField(upload_to='image') 
    image_name=models.CharField(max_length=60)
    image_caption=models.CharField(max_length=60)
    profile=models.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.IntegerField(default=0)
    comments=models.IntegerField(default=0)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update_image()

class Comment(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    comment = models.CharField(max_length=60)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

class Likes(models.Model):
    image=models.ForeignKey(Image, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    
