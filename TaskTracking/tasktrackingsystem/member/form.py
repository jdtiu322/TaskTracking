from django import forms
from .models import Member
from leader.models import Leader
from user.models import User
from django.forms import PasswordInput
from django.contrib.auth.forms import AuthenticationForm


class MemberFormRegistration(forms.ModelForm):
    Password = forms.CharField(widget=PasswordInput(render_value=False))
    class Meta:
        model = Member
        fields = ['Username', 'Password', 'Email', 'Firstname', 'Lastname', 'MemberID', 'RoleName', 'LeaderID', 'AssignDate']



class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']
