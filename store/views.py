from django.shortcuts import render, redirect
from .forms import RegisterForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import StorageSerializer
from .models import StorageUnits
# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("index")
    else:
        form = RegisterForm()
    return render(response,'registration/register.html',{'form':form})

class StorageList(APIView):
    def get(self, request, format=None):
        all_storage = StorageUnits.objects.all()
        serializers = StorageSerializer(all_storage, many=True)
        return Response(serializers.data)

