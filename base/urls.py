from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from .views import *
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', auth_view.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='base/home.html'), name='logout'),
    path('userRegister/', user_register, name='user_register'),
    path('events/', RecipeListviewevent.as_view(), name='Recipe'),
]