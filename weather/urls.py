from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60)(views.home), name='home'),
    path('accounts/register/', cache_page(60)(views.registerPage), name='register'),
    path('accounts/login/', cache_page(60)(views.auth), name='login'),
    path('accounts/verify', cache_page(60)(views.verify), name='verify'),
    path('accounts/logout/', cache_page(60)(views.logoutUser), name='logout'),
    path('weather/', cache_page(60)(views.weather), name='weather'),
    path('air-pollution/', cache_page(60)(views.air_pollution), name='air-pollution'),
    path('contact/', cache_page(60)(views.contact), name='contact'),
    path('success/', cache_page(60)(views.success), name='success'),
    path('accounts/subscribe', cache_page(60)(views.subscribe), name='subscribe')
]
