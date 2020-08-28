from django.urls import path,include
from django.conf.urls import url
from django.contrib.auth.views import LogoutView, LoginView
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('customer_register/', views.customer_register.as_view(), name='customerregister'),
    path('employee_register/', views.employee_register.as_view(), name='employeeregister'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/storage',views.StorageList.as_view()),
    path('profile/<username>/',views.profile, name='profile'),
    path('profile/<username>/update/',views.update_profile, name='update_profile'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('new-slot/', views.add_slot, name='new-slot'),
    path('slot-info/<username>/', views.slots_info, name='slots-info'),
    path('delivery/', views.delivery, name='delivery'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)





