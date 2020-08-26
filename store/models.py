from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class StorageUnits(models.Model):
    slots = models.CharField(max_length=100)
    type_of_goods = models.CharField(max_length=50)
    start_date_of_storage = models.DateTimeField(default=timezone.now)

    

class Goods(models.Model):
    goods_types = [
        (1,'fragile'),
        (2,'robust'), 
        (3,'perishable'),
    ]
    type = models.CharField(max_length=50, choices=goods_types)

    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='media/')
    items = models.TextField()
    contact = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'{self.user.username} '

    @classmethod
    def get_all_userprofiles(cls):
        return cls.objects.all()
    
