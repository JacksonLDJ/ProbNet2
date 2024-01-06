from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import RegexValidator
from .models import Customer_Data

#Forms which are used for the login page of the website.

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))


ip_validator = RegexValidator(
    regex=r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$',
    message='Enter a valid IP address.',
    code='invalid_ip'
)

ip_validator_range = RegexValidator(
    regex=r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?:\/[0-9]{1,2})?$',
    message='Enter a valid IP address.',
    code='invalid_ip'
)

#Forms used for Device Scan and Netsweeper scans.
class NmapForm(forms.Form):
    ip_address = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'IP Address',
            'class': 'w-full py-4 px-6 rounded-xl'
        }),
        label='Enter Your IP Range', 
        max_length=255,
        validators=[ip_validator])
#https://stackoverflow.com/questions/29247654/python-how-to-use-constructor-with-django-form-class

class NetsweeperForm(forms.Form):
    customer_drop_down = forms.ChoiceField(choices=[], required=False)
    ip_range = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'IP Address',
            'class': 'w-full py-4 px-6 rounded-xl'
        }),
        label='Enter Your IP Range',
        max_length=255,
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(NetsweeperForm, self).__init__(*args, **kwargs)
        customers = Customer_Data.objects.all().values('company_name', 'id')
        choices = [(-1, 'None')]
        for item in customers:
            something = (item['id'], item['company_name'])
            choices.append(something)
        self.fields['customer_drop_down'].choices = choices
    

class CustomerForm(forms.Form): 

    company_name = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Company Name',
            'class': 'w-64 py-4 px-6 rounded-xl'
        }),
        label='Enter Company Name:', 
        max_length=255,)
    
    location = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Company Location',
            'class': 'w-64 py-4 px-6 rounded-xl'
        }),
        label='Enter Company Name:', 
        max_length=255,)
    
    contact_name = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Contact name',
            'class': 'w-64 py-4 px-6 rounded-xl'
        }),
        label='Enter the contact name:', 
        max_length=255,)
    
    contact_position = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Contact Position',
            'class': 'w-64 py-4 px-6 rounded-xl'
        }),
        label='Enter the role of the contact', 
        max_length=255,)
    
    contact_number = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Contact Number',
            'class': 'w-64 py-4 px-6 rounded-xl'
        }),
        label='Phone Number for Contact', 
        max_length=255,)
    
    initial_ip_range = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Intitial IP range',
            'class': 'w-64 py-4 px-6 rounded-xl'
        }),
        label='Enter the IP for customer IP range', 
        max_length=255)