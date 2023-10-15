from django.urls import path
from . import views
# Create your views here.
app_name = 'project'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('registration.html',views.ProjectRegistration.as_view(), name='registration'),
    path('login.html/', views.ProjectLogin.as_view(), name='login'),
]