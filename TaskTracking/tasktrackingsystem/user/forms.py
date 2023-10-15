from django.forms import ModelForm
from .models import User,login
from django import forms


class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'Username',
            'Password',
            'Email',
            'Firstname',
            'Lastname'
        ]
class LoginForm(ModelForm):
    class Meta:
        model = login
        fields = [
            'Username',
            'Password',
        ]


