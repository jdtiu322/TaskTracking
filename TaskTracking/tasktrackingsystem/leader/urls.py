from django.urls import path
from . import views


app_name = 'leader'
urlpatterns = [
    path('leader_registration/', views.LeaderRegistration.as_view(), name='registration'),

]
