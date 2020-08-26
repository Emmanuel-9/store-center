from django.shortcuts import render, redirect
from .forms import RegisterForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import StorageSerializer
from .models import StorageUnits
<<<<<<< HEAD
=======
from .permissions import IsAdminOrReadOnly
from django.contrib.auth.decorators import login_required

>>>>>>> d27a2d29d540455941b900ab5408b6f0bc00f000
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

<<<<<<< HEAD
class StorageList(APIView):
    def get(self, request, format=None):
        all_storage = StorageUnits.objects.all()
        serializers = StorageSerializer(all_storage, many=True)
        return Response(serializers.data)

=======

class StorageList(APIView):
    def get(self, request, format=None):
        all_merch = StorageUnits.objects.all()
        serializers = StorageSerializer(all_merch, many=True)
        return Response(serializers.data)    
        permission_classes = (IsAdminOrReadOnly,)
>>>>>>> d27a2d29d540455941b900ab5408b6f0bc00f000
