from django.contrib.auth.forms import AuthenticationForm
from django.forms import PasswordInput
from .models import Project
from leader.models import Leader
from django import forms


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['ProjectID', 'ProjectName', 'LeaderID', 'StartDate', 'Deadline']


class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']
