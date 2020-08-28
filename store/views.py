from django.shortcuts import render, redirect, get_object_or_404
from .forms import EditProfileForm,SlotsForm,CategoryForm,CustomerSignUpForm,EmployeeSignUpForm, DeliveryForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import StorageSerializer
from .models import StorageUnits,UserProfile,Slot,Category,User
from .permissions import IsAdminOrReadOnly
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
# Create your views here.


def home(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
    else:
        form = CategoryForm()
    try:
        categories = Category.objects.all()
    except Category.DoesNotExist:
        categories = None
    params = {
        'categories': categories,
        'form': form,
    }

    return render(request, 'index.html', params)

def register(request):
    return render(request, 'registration/register.html')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'registration/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = 'registration/employee_register.html'


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class StorageList(APIView):
    def get(self, request, format=None):
        all_merch = StorageUnits.objects.all()
        serializers = StorageSerializer(all_merch, many=True)
        return Response(serializers.data)    
        permission_classes = (IsAdminOrReadOnly,)

def profile(request, username):
    try:
        user = User.objects.get(pk = username)
        profile = UserProfile.objects.get(user = user)
        slots = Slot.get_user_slots(profile.id)
        slots_count = slots.count()
    except Slot.DoesNotExist:
        slots = None
    return render(request, 'profile.html',{'slots': slots, 'count': slots_count})
    
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

@login_required(login_url='/accounts/login/')
def add_slot(request):
    if request.method == 'POST':
        form = SlotsForm(request.POST, request.FILES)
        if form.is_valid():
            slot = form.save(commit=False)
            slot.user = request.user.userprofile
            slot.save()
            return redirect('home')
    else:
        form = SlotsForm()
    return render(request, 'bookslot.html', {'form': form})

@login_required(login_url='/accounts/login/')
def slots_info(request, username):
    try:
        user = User.objects.get(pk = username)
        profile = UserProfile.objects.get(user = user)
        slots = Slot.get_user_slots(profile.id)
        slots_count = slots.count()
    except Slot.DoesNotExist:
        slots = None
    return render(request, 'slotsinfo.html',{'slots': slots, 'count': slots_count})


def delivery(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST, request.FILES)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.user = request.user.userprofile
            delivery.save()
            return redirect('home')
    else:
        form = DeliveryForm()
    return render(request, 'delivery.html', {'form': form})

