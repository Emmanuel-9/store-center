from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,UserProfile,Slot,Category,Delivery
from .models import User,Employee,Customer,UserProfile,Slot,Category, Delivery,Pickup
from django.db import transaction



class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        customer= Customer.objects.create(user=user)
        customer.save()
        return user
    


class EmployeeSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        employee= Employee.objects.create(user=user)
        employee.save()
        return user


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'items', 'contact', 'email','location_address']

class SlotsForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = ['name_of_good', 'image_of_good', 'mass_of_good_in_kgs']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image', 'cost', 'slots_remaining']

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        exclude = []

class PickupForm(forms.ModelForm):
    class Meta:
        model = Pickup
        fields = ['contact', 'email',  'name_of_good', 'date_of_pickup', 'time_of_pickup']

