from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('', views.home, name="home"),
    path('home_page', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('loginp/', auth_views.LoginView.as_view(template_name='loginp.html'), name='loginp'),
    path('logind/', auth_views.LoginView.as_view(template_name='logind.html'), name='logind'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('appointment/',views.appointment, name = "appointment"),
    path('doctors', views.doctors, name = "doctors")
]
