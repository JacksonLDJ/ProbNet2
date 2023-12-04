from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def app_home(request):
    return render(request, 'nmap_scanner/app_home.html')


def contact(request):
    return render(request, 'core/contact.html')


def login(request):        
        return render (request, 'core/login.html')

def logout(request):
     logout(request)
     return "core/login.html"

@login_required
def NMAP_Scan(request):
     return render(request, 'nmap_scanner/NMAP_Scan.html')

@login_required
def Full_Scan_History(request):
     return render(request, 'nmap_scanner/Full_Scan_History.html')

@login_required
def Quick_Scan_History(request):
     return render(request, 'nmap_scanner/Quick_Scan_History.html')

