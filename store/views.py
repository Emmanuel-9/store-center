from django.shortcuts import render, redirect
from .forms import RegisterForm
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
