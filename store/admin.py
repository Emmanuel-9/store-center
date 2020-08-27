from django.contrib import admin
from .models import Goods,StorageUnits,UserProfile,Category

# Register your models here.
admin.site.register(Goods)
admin.site.register(StorageUnits)
admin.site.register(UserProfile)
admin.site.register(Category)
