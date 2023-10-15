from django import forms
from leader.models import Leader
from user.models import User
from django.forms import PasswordInput
from django.contrib.auth.forms import AuthenticationForm


class LeaderFormRegistration(forms.ModelForm):
    Password = forms.CharField(widget=PasswordInput(render_value=False))
    class Meta:
        model = Leader
        fields = ['Username', 'Password', 'Email', 'Firstname', 'Lastname']


