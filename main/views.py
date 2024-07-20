from django.shortcuts import render
from django.http import HttpResponse


from utils.weather_request import weather_find
from main.models import UserRequestModel

from loguru import logger

def index(request):
    return render(request, 'main/index.html')



def weather_info(request):
    try:
        if request.method == 'POST':
    # Получаем данные из формы
            city = request.POST.get('city')
            weather_info=weather_find(city)
            current_temperature = weather_info[0]
            time = str(weather_info[1])
            
            
            
            user_object = UserRequestModel(city=city, current_temperature=current_temperature, time=time)
            user_object.save()



            context = {
                "current_temperature": current_temperature,
                "city": city,
                "time": time,
            }
            
            
    
            return render(request, 'main/weather.html', context=context)
        
        else:
    # Если это не POST-запрос, отображаем форму
            return render(request, 'main/index.html')
    except:
        return render(request, 'main/index.html')
