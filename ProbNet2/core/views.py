from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import NmapForm
from ProbNet2.scanner import NMAP_Scanner
from core.data import get_device_data, get_ports_by_device

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
     return render(request, 'nmap_scanner/search.html')

@login_required
def Quick_Scan_History(request):
     return render(request, 'nmap_scanner/netsweeper_scan.html')

@login_required
def reporting_devices(request):
     
     return render(request, 'nmap_scanner/reporting/devices.html', {
          "data":get_device_data()
     })

@login_required
def reporting_ports(request, device_id):
     
     return render(request, 'nmap_scanner/reporting/ports.html', {
          "data":get_ports_by_device(device_id)
     })


@login_required
def perform_nmap_scan(request):
    if request.method == 'POST':
        form = NmapForm(request.POST)
        if form.is_valid():
            # Get the IP range from the form
            ip_address = form.cleaned_data['ip_address']

            # Perform NMAP scan
            nmap_scanner = NMAP_Scanner()
            scan_result = nmap_scanner.NMAP_Scan_And_Save(ip_address)

            # Redirect to a page displaying the scan result or any other appropriate page
            return HttpResponseRedirect('/app_home/')
    else:
        form = NmapForm()

    return render(request, 'app_home.html', {'form': form})

@login_required

def netsweeper(request):
     if request.method == 'POST':
        form = NmapForm(request.POST)
        if form.is_valid():
            # Get the IP range from the form
            ip_range = form.cleaned_data['ip_range']

            nmap_scanner = NMAP_Scanner()
            nmap_scanner.netsweeper(ip_range)


            
