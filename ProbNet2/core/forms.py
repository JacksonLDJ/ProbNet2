from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import RegexValidator

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


class NetsweeperForm(forms.Form):
    ip_range = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'IP Address',
            'class': 'w-full py-4 px-6 rounded-xl'
        }),
        label='Enter Your IP Range', 
        max_length=255,
        validators=[ip_validator_range])