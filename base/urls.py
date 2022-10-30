from django.urls import path
from . import views
from django.contrib import admin

urlpatterns=[
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
]
