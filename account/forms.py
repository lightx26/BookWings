from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['phone_number', 'email', 'password', 'first_name', 'last_name']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Phone number or email")
