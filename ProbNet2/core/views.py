from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, FileResponse
from .forms import NmapForm, NetsweeperForm, CustomerForm
from ProbNet2.scanner import NMAP_Scanner
from core.data import get_device_data, get_ports_by_device, get_netsweeper_results, get_customer_data
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
from core.models import Customer_Data
from core.models import Device_Data, OS_Info, Netsweeper_Result

#Resources used: https://docs.djangoproject.com/en/5.0/topics/http/views/ | https://docs.djangoproject.com/en/5.0/howto/outputting-pdf/ | https://www.geeksforgeeks.org/generate-a-pdf-in-django/

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
     return render(request, 'nmap_scanner/NMAP_Scan.html', {
         'form':NmapForm
     })


#Renders the Netsweeper page and provides the dropd down menu for customers within the netsweeper_scan.html page
@login_required
def Quick_Scan_History(request):
     customers = Customer_Data.objects.all().values('company_name', 'id') #Only pull out the data we need, more secure.
     choices = [(-1, 'None')]
     for item in customers:
          choice = (item['id'], item['company_name'])
          choices.append(choice)

     form = NetsweeperForm()
     form.fields['customer_drop_down'].choices = choices
     return render(request, 'nmap_scanner/netsweeper_scan.html',{
         'form':form 
     })

#Renders the customer reports page
@login_required
def reporting_customer(request):
     return render(request, 'nmap_scanner/reporting/customer_info.html', {
          "data":get_customer_data()
     })
#Render the device reports page
@login_required
def reporting_devices(request):
     
     return render(request, 'nmap_scanner/reporting/devices.html', {
          "data":get_device_data()
     })

#Renders the ports reports page
@login_required
def reporting_ports(request, device_id):
     
     return render(request, 'nmap_scanner/reporting/ports.html', {
          "data":get_ports_by_device(device_id)
     })

#Renders the Netsweeper reports page
@login_required
def reporting_netsweeper(request):

    return render(request, 'nmap_scanner/reporting/netsweeper_results.html',{
                  "data": get_netsweeper_results()})

#Logic to perform NMAP Scan, uses the NMAP_Scanner class in ProbNet2>scanner.py and NmapForm Core>forms.py to perform the scan.
@login_required
def perform_nmap_scan(request):
    if request.method == 'POST':
        form = NmapForm(request.POST)
        if form.is_valid():
            # Get the IP address from the form
            ip_address = form.cleaned_data['ip_address']

            # Perform NMAP scan
            nmap_scanner = NMAP_Scanner()
            scan_result = nmap_scanner.NMAP_Scan_And_Save(ip_address)

            # Redirect to a page displaying the reporting section.
            return HttpResponseRedirect('/reporting/devices/')
    else:
        form = NmapForm()

    return render(request, 'nmap_scanner/NMAP_Scan.html', {'form': form})

def customer_data(request):
     form = CustomerForm()
     
     return render(request, 'nmap_scanner/customer_data.html', {'form': form})


#Function to perform the netswepper scan, it takes the IP address from the inittial_ip range and performs the netsweeper scan within scanner.py
def netsweeper(request):
    form = NetsweeperForm()

    if request.method == 'POST':
        form = NetsweeperForm(request.POST)
        if form.is_valid():
            # Get the IP range from the form
            customer_id = form.cleaned_data['customer_drop_down']
            #Checks what the customer choice is
            if customer_id != '-1':
                customer = Customer_Data.objects.get(id=customer_id)
                ip_range = customer.initial_ip_range
            else:
                ip_range = form.cleaned_data['ip_range'] #Originally there was going to be the option of entering a different range, this was then changed.

            nmap_scanner = NMAP_Scanner()
            nmap_scanner.netsweeper(ip_range, customer_id)

            return HttpResponseRedirect('/reporting/netsweeper_results/')

    return render(request, 'nmap_scanner/reporting/netsweeper_results.html', {'form': form})

#Writes the data to the customer_database once the user clicks submit on the CustomerForm
@login_required
def submit_customer_data(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            
            company_name = form.cleaned_data['company_name']
            location = form.cleaned_data['location']
            contact_name = form.cleaned_data['contact_name']
            contact_position = form.cleaned_data['contact_position']
            contact_number = form.cleaned_data['contact_number']
            initial_ip_range = form.cleaned_data['initial_ip_range']

            customer = Customer_Data.objects.create(
                company_name = company_name,
                location = location,
                contact_name = contact_name,
                contact_position = contact_position,
                contact_number = contact_number,
                initial_ip_range = initial_ip_range
            )

            customer.save()

            return HttpResponseRedirect('/customer_data_report/')

    return render(request, 'nmap_scanner/customer_data.html', {'form': form})

            


@login_required
#Resources used for PDF Gen: https://docs.djangoproject.com/en/5.0/howto/outputting-pdf/ | https://www.geeksforgeeks.org/generate-a-pdf-in-django/
#Form to generate a PDF for the device data table.
def generate_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    try:
        device_data = Device_Data.objects.all()
    except Device_Data.DoesNotExist:
        device_data = []

    for device in device_data:
        os_info = device.Operating_System  # Retrieve the related OS_Info instance

        # Add an empty line as a separator between IP addresses
        textob.textLine('')

        # Host Information - Pulls from the Device_Data model for data.
        textob.textLine(f"IP Address: {device.IP_Address}")
        textob.textLine(f"Created On: {device.created_on.strftime('%Y-%m-%d %H:%M:%S')}")
        textob.textLine(f"MAC Address: {device.MAC_Address}")
        textob.textLine(f"Hardware Details: {device.Hardware_Details if device.Hardware_Details else 'None'}")

        # OS_Info information - pulls from OS_Info model for data | If blank it returns nothing.
        textob.textLine(f"Operating System Type: {os_info.type if os_info else ''}")
        textob.textLine(f"Operating System Vendor: {os_info.vendor if os_info else ''}")
        textob.textLine(f"Operating System Family: {os_info.osfamily if os_info else ''}")
        textob.textLine(f"Operating System Generation: {os_info.osgen if os_info else ''}")
        textob.textLine(f"Operating System Accuracy: {os_info.accuracy if os_info else ''}")

    c.drawText(textob)
    c.showPage()
    c.save()

    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename="individual_device_scan.pdf")

@login_required
#Resources used for PDF Gen: https://docs.djangoproject.com/en/5.0/howto/outputting-pdf/ | https://www.geeksforgeeks.org/generate-a-pdf-in-django/
#This function was created but was taken out due to issues with the PDF formatting.
def netsweeper_generate_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    try:
        results_data = Netsweeper_Result.objects.all()
    except Netsweeper_Result.DoesNotExist():
        results_data = []

    for result in results_data:
        
            textob.textLine('')

            textob.textLine(f"IP Address: {result.ip_address if result else ''}")
            textob.textLine(f"MAC Address: {result.mac_address if result else ''}")
            textob.textLine(f"Hostname: {result.hostname if result else ''}")
            textob.textLine(f"Vendor: {result.vendor if result else ''}")
            textob.textLine(f"State: {result.state if result else ''}")
                

    c.drawText(textob)
    c.showPage()
    c.save()

    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename="netsweeper_results.pdf")






            
