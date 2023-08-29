from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement #импортировал свою модель
from .forms import AdvertisementForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth import decorators
def index(request):
    advertisiment=Advertisement.objects.all()
    contex={'advertisiments': advertisiment}
    return render(request, 'index.html', contex)
def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement =form.save(commit=False)
            new_advertisement.user=request.user
            new_advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form=AdvertisementForm()
    context={'form':form}
    return render(request, 'advertisement-post.html', context)
def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')
def profile(request):
    return render(request, 'profile.html')




