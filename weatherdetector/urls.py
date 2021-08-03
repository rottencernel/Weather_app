from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

handler404 = 'weather.views.handler_not_found'
