from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


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
        return f'{self.user.username}'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

class Slot(models.Model):
    image_of_good = models.ImageField(upload_to='slots/')
    name_of_good = models.CharField(max_length=250)
    mass_of_good_in_kgs = models.IntegerField(blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='slots')
    added = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        return f"/slot/{self.id}"

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def __str__(self):
        return f'{self.user.name} Slot'
    
    @classmethod
    def get_user_slots(cls,user):
        return cls.objects.filter(user=user)

    
    
