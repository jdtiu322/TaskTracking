from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .form import MemberFormRegistration
from django.urls import reverse
from django.shortcuts import redirect
from user.models import User


def css(request):
    return render(request, 'member_registration.html')

def index(request):
    return render(request, 'index.html')

class MemberRegistration(View):
    template_name = "member_registration.html"

    def get(self, request):
        member_form = MemberFormRegistration()
        return render(request, self.template_name, {'form': member_form})

    def post(self, request):
        member_form = MemberFormRegistration(request.POST)
        if member_form.is_valid():
            username = member_form.cleaned_data.get('Username')
            if User.objects.filter(Username=username).exists():
                return HttpResponse('<script>alert("Username already exist. Please try another username!"); '
                                    'window.location.href="{0}";</script>'.format(
                    reverse('member:member_registration')))

            new_member = member_form.save(commit=False)
            new_member.save()

            # Registration is successful, show the success popup
            return HttpResponse(
                '<script>alert("Registration Successful!"); window.location.href="{0}";</script>'.format(
                    reverse('member:member_login')))

        return render(request, self.template_name, {'form': member_form})


class MemberLogin(View):
    template_name = "member_login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log in the user
            login(request, form.get_user())
            return HttpResponse("Login successful!")

        # If form is not valid, display the login form again with errors
        return render(request, self.template_name, {'form': form})
