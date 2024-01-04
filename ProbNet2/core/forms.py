from django import forms
from django.contrib.auth.forms import AuthenticationForm



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))


error_message = {
    'invalid_login' : 'Invalid login credentials Please try again.'
}


class NmapForm(forms.Form):
    ip_address = forms.CharField(label='Enter Your IP Range', max_length=255)

class Netsweeper(forms.Form):
    ip_range = forms.CharField(label='Enter Your IP Range', max_length=255)