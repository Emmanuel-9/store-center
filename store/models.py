from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    email = models.EmailField(blank=True)

class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    email = models.EmailField(blank=True)


class StorageUnits(models.Model):
    slots = models.IntegerField()
    type_of_goods = models.CharField(max_length=50)
    start_date_of_storage = models.DateTimeField(default=timezone.now)

    def save_units(self):
        self.save()

    def delete_units(self):
        self.delete()    
class Goods(models.Model):
    goods_types = [
        (1,'fragile'),
        (2,'robust'), 
        (3,'perishable'),
    ]
    type = models.CharField(max_length=50, choices=goods_types)


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories/')
    cost = models.IntegerField(blank=False)
    slots_remaining = models.IntegerField(null=True, blank=False)

    def __str__(self):
        return f'{self.name} category'

    def create_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def find_category(cls, category_id):
        return cls.objects.filter(id=category_id)    

    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='media/',default='porsche.jpeg')
    items = models.TextField()
    contact = models.CharField(max_length=50)
    email = models.EmailField()
    location_address = models.CharField(max_length=300, null=True) 
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

    def create_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()



class Slot(models.Model):
    image_of_good = models.ImageField(upload_to='slots/')
    name_of_good = models.CharField(max_length=250)
    mass_of_good_in_kgs = models.IntegerField(blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='slots')
    added = models.DateTimeField(auto_now_add=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return f"/slot/{self.id}"
 
    def save_slot(self):
        self.save()

    def delete_slot(self):
        self.delete()

    def __str__(self):
        return f'{self.user} Slot'
    
    @classmethod
    def get_user_slots(cls,user):
        return cls.objects.filter(user=user)
    
    @classmethod
    def get_category_slots(cls,category):
        return cls.objects.filter(category=category)
    
    @classmethod
    def all_slots(cls):
        return cls.objects.all()

    @classmethod
    def find_slot(cls, slot_id):
        return cls.objects.filter(id=slot_id) 



class Delivery(models.Model):
    contact = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    email = models.EmailField()
    items = models.TextField()

class Pickup(models.Model):
    name_of_good = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=50)
    email = models.EmailField()
    date_of_pickup = models.DateField()
    time_of_pickup =models.TimeField(auto_now=False, auto_now_add=False)

