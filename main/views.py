from django.shortcuts import redirect, render
from django.http import HttpResponse

from utils.weather_request import weather_find
from main.models import UserRequestModel


def index(request):
    return render(request, 'main/index.html')



def weather_info(request):
    
    if request.method == 'POST':
 # Получаем данные из формы
 
        city = request.POST.get('city')
        current_temperature = weather_find(city)
        
        user_object = UserRequestModel(city=city, current_temperature=current_temperature)
        user_object.save()
 # Возвращаем результат на новую страницу
 
        return redirect('main/weather.html')
    
    else:
 # Если это не POST-запрос, отображаем форму
        return render(request, 'main/index.html')

