from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User,UserProfile

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1","password2"]

class EditProfileForm(forms.Form):
    email = forms.EmailField() 
    contact = forms.CharField()
    profile_picture = forms.ImageField()  