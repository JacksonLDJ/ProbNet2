from django.contrib import admin
from django.urls import path
from core.views import app_home, contact, logout, perform_nmap_scan, Full_Scan_History, Quick_Scan_History, NMAP_Scan, netsweeper, reporting_devices, reporting_ports, generate_pdf, reporting_netsweeper, netsweeper_generate_pdf, customer_data, submit_customer_data
from django.contrib.auth.views import LoginView, LogoutView
from core.forms import LoginForm
#Resources used: https://docs.djangoproject.com/en/5.0/topics/http/urls/



urlpatterns = [
    path('app_home/', app_home, name='app_home'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='home',),
    path ('NMAP_Scan/', NMAP_Scan, name='NMAP_Scan' ),
    path ('perform_nmap_scan/', perform_nmap_scan, name='perform_nmap_scan' ),
    path ('search/', Full_Scan_History, name='search' ),
    path ('netsweeper_scan/', Quick_Scan_History, name='netsweeper_scan' ),
    path ('netsweeper/', netsweeper, name='netsweeper' ),
    path ('reporting/devices/', reporting_devices, name='reporting_devices' ),
    path ('reporting/ports/<int:device_id>/', reporting_ports, name='reporting_ports' ),
    path ('reporting/netsweeper_results/', reporting_netsweeper, name="reporting_netsweeper" ),
    path ('generate_pdf/', generate_pdf, name="generate_pdf" ),
    path ('netsweeper_generate_pdf/', netsweeper_generate_pdf, name="netsweeper_generate_pdf" ),
    path ('customer_data/', customer_data, name="customer_data" ),
    path ('customer_data_save/', submit_customer_data, name="submit_customer_data"  )
]
