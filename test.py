import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ["OWM_API_KEY"]
OWM_ENDPOINT = "http://api.openweathermap.org/geo/1.0/direct"


def get_lat_lon(city_name, state_code, country_code, API_key):
  resp = requests.get(f"{OWM_ENDPOINT}?q={city_name},{state_code},{country_code}&appid={API_key}")
  data = resp.json()
  location = data[0]
  return location.get('lat'), location.get('lon')


print(get_lat_lon("Miami", "FL", "US", api_key))
