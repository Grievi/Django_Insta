from django.db import models
import datetime as dt
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500)
    profile_photo = models.ImageField(upload_to='media/', default='default.png')

    def __str__(self):
        return f'{self.user.username} Profile'#User.username

    def save_profile(self):
        self.save()

    def update_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    