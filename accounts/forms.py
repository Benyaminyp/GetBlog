from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    '''Custom sign-up form that creates a new user with email as the only required field.'''
    class Meta:
        model = CustomUser
        fields = ("email",)