from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.


def app_home(request):
    return render(request, 'core/app_home.html')


def contact(request):
    return render(request, 'core/contact.html')


def login(request):        
        return render (request, 'core/login.html')
