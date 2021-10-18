from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='moringa')
        self.user.save()

        self.profile_test= Profile(id=1, name="image", profile_photo='default.jpg', bio='Welcome to my Channel', user=self.user)
