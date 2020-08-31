from django.contrib import admin
<<<<<<< HEAD
from .models import Goods,StorageUnits,UserProfile,Category,Slot,Delivery
from .models import Goods,StorageUnits,UserProfile,Category,Slot,User,Customer,Employee, Delivery

=======
from .models import Goods,StorageUnits,UserProfile,Slot
>>>>>>> feature-profile

# Register your models here.
admin.site.register(Goods)
admin.site.register(StorageUnits)
admin.site.register(UserProfile)
<<<<<<< HEAD
admin.site.register(Category)
admin.site.register(Slot)
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Delivery)
=======
admin.site.register(Slot)

>>>>>>> feature-profile
