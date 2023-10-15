from django.urls import path
from . import views

appName = 'User'
urlpatterns =[
    #path('', views.LoginForm, name='login')
    path('registration', views.registration, name='registration')
]
