from django import forms
from django.contrib.auth.forms import AuthenticationForm



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))


error_message = {
    'invalid_login' : 'Invalid login credentials Please try again.'
}