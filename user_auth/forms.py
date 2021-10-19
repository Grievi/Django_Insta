from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from typing import Sequence

class UserRegisterForm(UserCreationForm):
    
    class Meta:
        
        model=User
        fields = ('username','email','password1','password2')
        # widgets={
        #     'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}),
        #     'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'title- tag of the blog'}),
        #     'password1': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Your Password'}),
        #     'password2': forms.PasswordInput(attrs={'class':'form-control','placeholder':'confirm your password'}),
        # }