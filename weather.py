import requests
import os
from dotenv import load_dotenv
from dataclasses import dataclass


load_dotenv()
API_KEY = os.environ["OWM_API_KEY"]
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

@dataclass
class WeatherData:
    main: str
    description: str
    latitude: float
    longitude: float
    temperature: int

def get_lat_lon(city_name, state_code, country_code, API_KEY):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_KEY}')
    data = resp.json()
    if data:
        location = data[0]
        return location.get('lat'), location.get('lon')
    else:
        return None, None


def get_current_weather(lat, lon, API_KEY):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"
    }
    resp = requests.get(OWM_ENDPOINT, params=params)
    data = resp.json()
    weather = data["weather"][0]
    main = weather["main"]
    description = weather["description"]
    latitude = float(data["coord"]["lat"])
    longitude = float(data["coord"]["lon"])
    temperature = int(data["main"]["temp"])
    return WeatherData(main, description, temperature, latitude, longitude)


def main(city_name, state_name, country_name):
    lat, lon = get_lat_lon(city_name, state_name, country_name, API_KEY)
    weather_data = get_current_weather(lat, lon, API_KEY)
    return weather_data

if __name__ == "__main__":
    lat, lon = get_lat_lon("Yakutsk", "YA", "RU", API_KEY)
    if lat is not None and lon is not None:
        weather_data = get_current_weather(lat, lon, API_KEY)
        if weather_data is not None:
            print(weather_data)
        else:
            print("Failed to retrieve weather data.")
    else:
        print("Failed to retrieve latitude and longitude.")
