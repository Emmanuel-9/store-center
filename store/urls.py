from django.urls import path,include
from django.conf.urls import url
from django.contrib.auth.views import LogoutView, LoginView
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('api/storage',views.StorageList.as_view())
<<<<<<< HEAD
=======
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

>>>>>>> d27a2d29d540455941b900ab5408b6f0bc00f000
]


