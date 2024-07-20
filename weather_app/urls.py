from django.contrib import admin
from django.urls import path

from main import views




urlpatterns = [
    path("", views.index, name="index"),
    path("weather_info/", views.weather_info, name="weather_info"),
    
]
