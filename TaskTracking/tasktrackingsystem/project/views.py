from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .form import ProjectForm
from django.urls import reverse
from django.shortcuts import redirect
from project.models import Project


def index(request):
    return HttpResponse("hello world")


class ProjectRegistration(View):
    template_name = "registration.html"

    def get(self, request):
        project_form = ProjectForm()
        return render(request, self.template_name, {'form': project_form})

    def post(self, request):
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            projectname = project_form.cleaned_data.get('ProjectName')
            if Project.objects.filter(ProjectName=projectname).exists():
                return HttpResponse(
                    '<script>alert("Project name already exist. Please try another Project name!"); window.location.href="{0}";</script>'.format(
                        reverse('project:registration')))

            new_member = project_form.save(commit=False)
            new_member.save()

            # Registration is successful, show the success popup
            return HttpResponse(
                '<script>alert("Project Registration Successful!"); window.location.href="{0}";</script>'.format(
                    reverse('project:registration')))

        return render(request, self.template_name, {'form': project_form})

class ProjectLogin(View):
    template_name = "login.html"

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
