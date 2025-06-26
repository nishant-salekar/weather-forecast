from django.shortcuts import render
import pandas as pd
from sklearn.linear_model import LinearRegression
import datetime

def weather_view(request):
    city = request.POST.get('city', 'London')
    df = pd.read_csv('weather.csv')
    latest = df.iloc[-1]
    context = {
        'location': city,
        'current_temp': latest['temperature'],
        'feels_like': latest['feels_like'],
        'humidity': latest['humidity'],
        'clouds': latest['clouds'],
        'description': latest['description'],
        'city': latest['city'],
        'country': latest['country'],
        'time': latest['time'],
        'wind': latest['wind'],
        'pressure': latest['pressure'],
        'visibility': latest['visibility'],
        'MinTemp': latest['min_temp'],
        'time1': latest['time'],
        'temp1': latest['temperature'],
        'hum1': latest['humidity'],
        'time2': latest['time'],
        'temp2': latest['temperature'],
        'hum2': latest['humidity'],
        'time3': latest['time'],
        'temp3': latest['temperature'],
        'hum3': latest['humidity'],
        'time4': latest['time'],
        'temp4': latest['temperature'],
        'hum4': latest['humidity'],
        'time5': latest['time'],
        'temp5': latest['temperature'],
        'hum5': latest['humidity'],
    }
    return render(request, 'weather.html', context)