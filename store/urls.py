from django.urls import path,include
from django.conf.urls import url
from django.contrib.auth.views import LogoutView, LoginView
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('account/', include('django.contrib.auth.urls')),
    path('api/storage',views.StorageList.as_view()),
]


