from django.shortcuts import render, redirect
from .forms import RegisterForm,EditProfileForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import StorageSerializer
from .models import StorageUnits,UserProfile
from .permissions import IsAdminOrReadOnly
from django.contrib.auth.decorators import login_required

# Create your views here.

login_required(login_url='/accounts/login/')
def home(request):

    return render(request, 'index.html', locals())

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
        return redirect("login")
    else:
        form = RegisterForm()
    return render(response,'registration/register.html',{'form':form})

class StorageList(APIView):
    def get(self, request, format=None):
        all_merch = StorageUnits.objects.all()
        serializers = StorageSerializer(all_merch, many=True)
        return Response(serializers.data)    
        permission_classes = (IsAdminOrReadOnly,)

def profile(request):
    profile = UserProfile.get_all_userprofiles()
    context = {
        'profiles': profile,
    }
    return render(request, 'profile.html',context)         

def update_profile(request):
    user = request.user
    if request.method == 'POST':
        edit_form = EditProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('profile.html')
    else:
        edit_form = EditProfileForm() 
    context = {
        'profile_form': edit_form,
    }           
    return render(request, 'edit_profile.html',context)
