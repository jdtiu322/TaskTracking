from django.urls import path
from . import views
from .views import MemberRegistration

app_name = 'member'
urlpatterns = [
    path('member_registration.html', views.MemberRegistration.as_view(), name='member_registration'),
    path('member_registration/', MemberRegistration.as_view(), name='member_registration'),
    path('member_login/', views.MemberLogin.as_view(), name='member_login'),
]