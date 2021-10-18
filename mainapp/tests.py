from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='moringa')
        self.user.save()

        self.profile_test= Profile(id=1, name="image", profile_photo='default.jpg', bio='Welcome to my Channel', user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_bio(self):
        profile=Profile.objects.get(bio='Hello Guys mind your own business')
        self.assertEqual(profile.bio, 'Hello Guys mind your own business')

class ImageTest(TestCase):
    def setUp(self):
        self.profile_test = Profile(name='moringa', user=User(username='Grievi'))
        self.profile_test.save()

        self.image_test = Image(image='default.png', name='test', caption='default test', user=self.profile_test)

    def test_insatance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        after = Profile.objects.all()
        self.assertTrue(len(after) < 1)


