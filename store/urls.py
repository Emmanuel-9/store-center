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
    path('api/storage',views.StorageList.as_view()),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/',views.profile, name='profile'),
    path('profile/update/',views.update_profile, name='update_profile'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('account/', include('django.contrib.auth.urls')),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)





