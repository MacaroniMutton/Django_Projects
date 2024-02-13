from django.http import HttpResponse
from django.shortcuts import render
from .models import Gun

# Create your views here.


def home(request):
    gun_list = Gun.objects.all()
    context = {
        "gun_list": gun_list
    }
    return render(request, 'guns/index.html', context)

def detail(request, gun_id):
    gun = Gun.objects.get(pk=gun_id)
    context = {
        "gun": gun
    }
    return render(request, 'guns/detail.html', context)