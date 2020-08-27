from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm,EditProfileForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import StorageSerializer
from .models import StorageUnits,UserProfile
from .models import StorageUnits
from django.contrib.auth.models import User
from .permissions import IsAdminOrReadOnly
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
# Create your views here.

# @login_required(login_url='/accounts/login/')
def home(request):

    return render(request, 'index.html', locals())

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
        return redirect("login")
    else:
        form = RegisterForm()
    return render(request,'registration/register.html',{'form':form})

class StorageList(APIView):
    def get(self, request, format=None):
        all_merch = StorageUnits.objects.all()
        serializers = StorageSerializer(all_merch, many=True)
        return Response(serializers.data)    
        permission_classes = (IsAdminOrReadOnly,)

def profile(request, username):
    return render(request, 'profile.html')         

def update_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        edit_form = EditProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('profile', user.id)
    else:
        edit_form = EditProfileForm(instance=request.user.userprofile) 
    context = {
        'profile_form': edit_form,
    }           
    return render(request, 'edit_profile.html',context)
