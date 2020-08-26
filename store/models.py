from django.db import models
from django.utils import timezone

# Create your models here.
class StorageUnits(models.Model):
    slots = models.CharField(max_length=100)
    type_of_goods = models.CharField(max_length=50)
    start_date_of_storage = models.DateTimeField(default=timezone.now)

class Goods(models.Model):
    goods_types = [
        (1,'fragile'),
<<<<<<< HEAD
        (2,'robust'), 
        (3,'perishable'),
    ]
    type = models.CharField(max_length=50, choices=goods_types)

class Profile(models.Model):
    username = models.CharField(max_length=50)
    items = models.TextField()
    contact = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

=======
        (2,'robust'),
        (3,'perishable'),
    ]
    type = models.CharField(max_length=50, choices=goods_types)
>>>>>>> d27a2d29d540455941b900ab5408b6f0bc00f000
