from django.shortcuts import render, redirect, get_object_or_404
from .forms import EditProfileForm,SlotsForm,CategoryForm,CustomerSignUpForm,EmployeeSignUpForm, DeliveryForm,PickupForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import StorageSerializer
from .models import StorageUnits,UserProfile,Slot,Category,User, Delivery
from .permissions import IsAdminOrReadOnly
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.http import HttpResponseRedirect

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


class register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'registration/customer_register.html'

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
def add_slot(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        form = SlotsForm(request.POST, request.FILES)
        if form.is_valid():
            slot = form.save(commit=False)
            slot.category = category
            slot.user = request.user.userprofile
            slot.save()
            return redirect('home')
    else:
        form = SlotsForm()
    return render(request, 'bookslot.html', {'form': form})

@login_required(login_url='/accounts/login/')
def slots_info(request, category_id, username):
    try:
        user = UserProfile.objects.get(user=username)
        category = Category.objects.get(id=category_id)
        slots = Slot.objects.filter(user=user,category=category)
        slot_count = slots.count()
    except Slot.DoesNotExist:
        slots = None

    return render(request, 'slotsinfo.html',{'slots': slots,  'count': slot_count})
    params = {
        'slots': slots, 
        'count': slot_count,
    }   
    return render(request, 'slotsinfo.html', params)


def employeeslots_info(request,category_id):
    try:
        category = Category.objects.get(id=category_id)
        employeeslots = Slot.objects.filter(category=category)
        countslots = employeeslots.count()
    except Slot.DoesNotExist:
        employeeslots = None
    return render(request, 'slotsinfo.html',{'employeeslots': employeeslots, 'countslots': countslots})


def delivery(request, slot_id):
    slot = Slot.objects.get(id=slot_id)
    if request.method == 'POST':
        form = DeliveryForm(request.POST, request.FILES)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.user = request.user.userprofile
            delivery.slot = slot
            delivery.save()
            return redirect('home')
    else:
        form = DeliveryForm()
    return render(request, 'delivery.html', {'form': form})

def card_delete(request, id):
    card_that_is_ready_to_be_deleted = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        card_that_is_ready_to_be_deleted.delete()

    return redirect('home')

def slot_delete(request, id):
    slot_that_is_ready_to_be_deleted = get_object_or_404(Slot, id=id)
    if request.method == 'POST':
        slot_that_is_ready_to_be_deleted.delete()

    return redirect('employeeslots-info')

def pick_up(request):
    if request.method == "POST":
        form = PickupForm(request.POST)
        if form.is_valid():
            pick_up = form.save(commit=False)
            pick_up.user= request.user
            pick_up.save()
            return redirect('home')
    else:
        form = PickupForm()
    return render(request, 'pickup.html', {'form': form})

def customer_delivery(request, slot_id):
    try:
        slot = Slot.objects.get(id=slot_id)
        customer = Delivery.objects.filter(slot=slot)
    except Delivery.DoesNotExist:
        customer = None
    return render(request, 'customerdelivery.html', {'customer': customer})

