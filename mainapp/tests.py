from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='moringa')
        self.user.save()

        self.profile_test= Profile(id=1, name="image", profile_photo='static/img/homepage.jpg', bio='Welcome to my Channel', user=self.user)

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

class TestLikes(TestCase):
    def setUp(self):
        user =User.objects.create(name='moringa',username='moringa',)

        Profile.objects.create(bio='Mind your bio',profile_photo='static/img/homepage.jpg')

        Image.objects.create(image_caption='test1',image='default.png',profile_id=user.id,user_id=user.id)

        Likes.objects.create(image_id=Image.image.id,user_id=user.id)
