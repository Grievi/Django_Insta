from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    username=models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    bio = models.CharField(max_length=500)
    profile_photo = models.ImageField(upload_to='media/', default='default.png')

    # def __str__(self):
    #     return f'{self.user.username} Profile'#User.username

    def save_profile(self):
        self.save()

    def update_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Image(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='image') 
    image_name=models.CharField(max_length=60)
    image_caption=models.CharField(max_length=60)
    profile=models.ForeignKey(on_delete=models.CASCADE)
    likes=models.IntegerField(default=0)
    comments=models.IntegerField(default=0)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

       