from django.contrib import admin
from django.urls import path
from core.views import app_home, contact, logout, NMAP_Scan, Full_Scan_History, Quick_Scan_History
from django.contrib.auth.views import LoginView, LogoutView
from core.forms import LoginForm




urlpatterns = [
    path('app_home/', app_home, name='app_home'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='home',),
    path ('NMAP_Scan/', NMAP_Scan, name='NMAP_Scan' ),
    path ('Full_Scan_History/', Full_Scan_History, name='Full_Scan_History' ),
    path ('Quick_Scan_History/', Quick_Scan_History, name='Quick_Scan_History' ),
]
