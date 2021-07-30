from django.core.mail import send_mail, BadHeaderError
from urllib.error import HTTPError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import ContactForm, CreateUserForm
from django.contrib import messages
from decouple import config
import urllib.request
import json


appid = config('appid')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for' + ' ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incrrect')

    return render(request, 'login.html', {})


def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'home.html', {})


def weather(request):
    data = {}
    if request.method == 'POST':
        city = request.POST['city']
        try:
            res = urllib.request.urlopen(
                f'http://api.openweathermap.org/data/2.5/weather?q={city}'
                f'&units=metric&appid={appid}'
            ).read()
            json_data = json.loads(res)

            data = {
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) +
                              ' ' +
                              str(json_data['coord']['lat']),
                "temp": str(json_data['main']['temp']) + 'c',
                "feels_like": str(json_data['main']['feels_like']) + 'c',
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity']),
                "wind": str(json_data['wind']['speed']) + 'm/s',
                'cloudiness': str(json_data['clouds']['all']) + '%',
            }

        except HTTPError:
            city = 'There is no such city'
        except UnicodeEncodeError:
            city = 'City name must be in English'
    else:
        city = ''

    return render(request, 'weather.html', {'city': city, 'data': data})


def air_pollution(request):
    data = {}
    air_quality = ''

    if request.method == 'POST':
        city = request.POST['city']
        try:
            lat, lon = get_coordinates(city)
            res = urllib.request.urlopen(
                f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}'
                f'&lon={lon}&appid={appid}'
            ).read()
            json_data = json.loads(res)

            data = json_data['list'][0]['components']
            air_quality = str(json_data['list'][0]['main']['aqi'])

        except HTTPError:
            city = 'there is no such city'
        except UnicodeEncodeError:
            city = 'City name must be in English'
    else:
        city = ''

    return render(request, 'air_pollution.html',
                  {'city': city, 'data': data, 'air_quality': air_quality})


def get_coordinates(city):
    res_to_get_coord = urllib.request.urlopen(
        f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={appid}'
    ).read()
    city_json_info = json.loads(res_to_get_coord)
    lat = str(city_json_info['coord']['lat'])
    lon = str(city_json_info['coord']['lon'])
    return lat, lon


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            subject = form.cleaned_data['subject']
            try:
                send_mail(subject, message, from_email, [config('EMAIL_HOST_USER')])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('success')
    return render(request, "contact.html", {'form': form})


def success(request):
    return render(request, 'success.html')


def handler_not_found(request, exception):
    return render(request, '404page.html')
