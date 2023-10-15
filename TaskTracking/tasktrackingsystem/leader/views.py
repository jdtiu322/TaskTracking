from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .form import LeaderFormRegistration
from django.urls import reverse
from django.shortcuts import redirect
from user.models import User


class LeaderRegistration(View):
    template_name = "member_registration.html"

    def get(self, request):
        leader_form = LeaderFormRegistration()
        return render(request, self.template_name, {'form': leader_form})

    def post(self, request):
        leader_form = LeaderFormRegistration(request.POST)
        if leader_form.is_valid():
            username = leader_form.cleaned_data.get('Username')
            if User.objects.filter(Username=username).exists():
                return HttpResponse(
                    '<script>alert("Username already exist. Please try another username!"); window.location.href="{0}";</script>'.format(
                        redirect('member:registration')))

            new_leader = leader_form.save(commit=False)
            new_leader.save()

            # Registration is successful, show the success popup
            return HttpResponse(
                '<script>alert("Registration Successful!"); window.location.href="{0}";</script>'.format(
                    reverse('leader:registration')))
            #
