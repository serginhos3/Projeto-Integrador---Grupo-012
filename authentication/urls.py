from django.contrib import admin
from django.urls import path, include
from . import views

# arquivo editado

urlpatterns = [
    path('', views.home, name="home"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
    path('administrador/', views.administrador, name="administrador"),
    path('treinamentos/', views.treinamentos, name="treinamentos"),
    path('perfil/', views.perfil, name="perfil"),
    path('termos/', views.termos, name="termos"),
    path('suporte/', views.suporte, name="suporte"),
]