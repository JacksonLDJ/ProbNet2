from django.contrib import admin
from django.urls import path
from core.views import home, contact
from django.contrib.auth.views import LoginView
from core.forms import LoginForm

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login')
]
