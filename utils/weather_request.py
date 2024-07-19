import openmeteo_requests
from openmeteo_sdk.Variable import Variable
import numpy as np

from city_to_coordinates import coordinates_find





om = openmeteo_requests.Client()



def weather_find(city: str):
    coordinates = coordinates_find(city)


    params = {
        "latitude": coordinates[0],
        "longitude": coordinates[1],
        "hourly": ["temperature_2m", "precipitation"],
        "current": ["temperature_2m"]
    }




    responses = om.weather_api("https://api.open-meteo.com/v1/forecast", params=params)
    response = responses[0]



    # Расчёт для текущей температуры
    current = response.Current()
    
    
    current_variables = list(map(lambda i: current.Variables(i), range(0, current.VariablesLength())))
    current_temperature_2m = next(filter(lambda x: x.Variable() == Variable.temperature and x.Altitude() == 2, current_variables))
    
    
    


    
    
    
    return int(current_temperature_2m.Value())
    







if __name__ == '__main__':
    print(weather_find('Нижний Новгород'))