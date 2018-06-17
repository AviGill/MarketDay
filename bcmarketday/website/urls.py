from django.urls import path
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    path('findmarket/', views.search, name='search'),
    path('loggedin/', views.loggedin, name='loggedin'),
    path('', views.home, name='home'),
    path('login/', login, {'template_name': 'website/login.html'}, name='login'),
    path('register/', views.register, name='register'),

    
 
  
    
] 