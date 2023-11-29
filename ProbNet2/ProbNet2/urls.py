from django.contrib import admin
from django.urls import path
from core.views import app_home, contact, logout
from django.contrib.auth.views import LoginView, LogoutView
from core.forms import LoginForm




urlpatterns = [
    path('app_home/', app_home, name='app_home'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='home', )
]
