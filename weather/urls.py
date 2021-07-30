from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('weather/', views.weather, name='weather'),
    path('air-pollution/', views.air_pollution, name='air-pollution'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
]