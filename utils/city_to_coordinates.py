from geopy.geocoders import Nominatim










# Функция получает город и отдает список широты и долготы, запрос может быть на русском или на английском
def coordinates_find(city:str):
    
    geolocator = Nominatim(user_agent="coordinates_find")
    
    location = geolocator.geocode(city)
    
    coordinates = [location.latitude, location.longitude]

    return ((coordinates))



