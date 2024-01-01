from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import NmapForm
from ProbNet2.scanner import NMAP_Scanner

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

@login_required
def perform_nmap_scan(request):
    if request.method == 'POST':
        form = NmapForm(request.POST)
        if form.is_valid():
            # Get the IP range from the form
            ip_range = form.cleaned_data['ip_range']

            # Perform NMAP scan
            nmap_scanner = NMAP_Scanner()
            scan_result = nmap_scanner.NMAP_Scan_And_Save(ip_range)

            # Redirect to a page displaying the scan result or any other appropriate page
            return HttpResponseRedirect('app_home.html')
    else:
        form = NmapForm()

    return render(request, 'app_home.html', {'form': form})