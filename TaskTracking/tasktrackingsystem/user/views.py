from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .forms import RegistrationForm, LoginForm



def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Success')
        else:
            return HttpResponse('Failed')
    else:
        form = RegistrationForm()

    return render(request,
                  'registration.html',
                  {'form': form}
                  )


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Registration succesful')
        else:
            return HttpResponse('Username already exists')
    else:
        form = LoginForm()

    return render(request,
        'login.html',
        {'form': form}
    )