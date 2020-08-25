from django.urls import path,include
from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('register/', views.register, name='register'),
    path('api/storage',views.StorageList.as_view())
]


