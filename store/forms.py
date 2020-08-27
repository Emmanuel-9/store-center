from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User,UserProfile,Slot

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ["username", "email", "password1","password2"]

class EditProfileForm(forms.ModelForm):
    slots = forms.CharField(max_length=300, help_text='Enter the slots of your goods')
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'items', 'contact', 'email']

class SlotsForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = ['name_of_good', 'image_of_good', 'mass_of_good_in_kgs']