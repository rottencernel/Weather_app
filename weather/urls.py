from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.registerPage, name='register'),
    path('accounts/login/', views.auth, name='login'),
    path('accounts/verify', views.verify, name='verify'),
    path('accounts/logout/', views.logoutUser, name='logout'),
    path('weather/', views.weather, name='weather'),
    path('air-pollution/', views.air_pollution, name='air-pollution'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('accounts/subscribe/', views.subscribe, name='subscribe')
]