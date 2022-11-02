from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', views.home, name="home"),
    path('home_page', views.home, name="home"),
    path('registerpatient/', views.registerPatient, name="registerPatient"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
