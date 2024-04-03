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
    # icon: str
    temperature: int

def get_lat_lon(city_name, state_code, country_code, API_key):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}')
    data = resp.json()
    if data:
        location = data[0]
        return location.get('lat'), location.get('lon')
    else:
        return "Invalid lat and lon response"


def get_current_weather(lat, lon, API_key):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_key,
        "units": "metric"
    }
    resp = requests.get(OWM_ENDPOINT, params=params)
    data = resp.json()
    weather = data["weather"][0]
    main = weather["main"]
    description = weather["description"]
    # icon = weather["icon"]
    temperature = int(data["main"]["temp"])
    return WeatherData(main, description, temperature)


def main(city_name, state_name, country_name):
    lat, lon = get_lat_lon(city_name, state_name, country_name, API_KEY)
    weather_data = get_current_weather(lat, lon, API_KEY)
    return weather_data

if __name__ == "__main__":
    lat, lon = get_lat_lon("New South Wales", "NSA", "AUS", API_KEY)
    if lat is not None and lon is not None:
        weather_data = get_current_weather(lat, lon, API_KEY)
        if weather_data is not None:
            print(weather_data)
        else:
            print("Failed to retrieve weather data.")
    else:
        print("Failed to retrieve latitude and longitude.")
