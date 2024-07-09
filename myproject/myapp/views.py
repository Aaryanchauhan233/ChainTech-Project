import datetime
import random
import requests
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

quotes = [
    "Life is what happens when you're busy making other plans.",
    "The purpose of our lives is to be happy.",
    "Life is really simple, but we insist on making it complicated.",
    "In the end, it's not the years in your life that count. It's the life in your years."
]

def get_random_quote():
    return random.choice(quotes)

def get_weather_data(location):
    api_key = '216f274b63e480c850d9f44738094ea0'  
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"{weather}, {temperature}°C"
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather: {e}"

def index(request):
    return render(request, 'myapp/index.html')

def get_weather(request):
    location = request.GET.get('location')
    if location:
        weather_info = get_weather_data(location)
        return JsonResponse({'weather': weather_info})
    else:
        return JsonResponse({'error': 'No location provided'}, status=400)

def get_quote(request):
    random_quote = get_random_quote()
    return JsonResponse({'quote': random_quote})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        return HttpResponse(f"Name: {name}, Email: {email}")
    return render(request, 'myapp/form.html') 