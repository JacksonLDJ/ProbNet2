from django.contrib import admin
from django.urls import path
from core.views import home, contact
from django.contrib.auth.views import LoginView
from core.forms import LoginForm
from django.urls import reverse_lazy

urlpatterns = [
    path('app_home/', home, name='app_home'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='home' )
]
