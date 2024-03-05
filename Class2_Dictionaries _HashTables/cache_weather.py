import requests
import time
import os

from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.') / '.env'
load_dotenv(dotenv_path=dotenv_path)

class WeatherCache:
    def __init__(self, expiry=300): #Cache expires after 5 minutes
        self.cache = {}
        self.expiry = expiry

    def get_lat_long(self, city):
        response = requests.get(
            f"https://geocode.xyz/{city}?json=1&auth={os.getenv('GEOCODE_API_KEY')}"
        )
        if response.status_code == 200:
            data = response.json()
            lat = data["latt"]
            lon = data["longt"]
            if lat and lon:
                return lat, lon
            else:
                print(f"Failed to get lat and long for {city}")
                return None, None
        else:
            print(f"Failed to get lat and long for {city}")
            return None, None

    def get_weather(self, lat, long):
        key = (lat, long)
        current_time = time.time()

        if key in self.cache:
            cached_data = self.cache[key]
            if current_time - cached_data["timestamp"] < self.expiry:
                print("Returning cached data")
                return cached_data["data"]
            else:
                print("Cache expired. Fetching new data1")
        else:
            print("Cache miss. Fetching new data2")

        weather_data = self.fetch_weather_data_from_api(lat, long)
        self.cache[key] = {"data": weather_data, "timestamp": current_time}
        return weather_data

    def fetch_weather_data_from_api(self, lat, lon):
        api_key = os.getenv('OPENWEATHER_API_KEY')
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            useful_data = {
                'coord': data.get('coord', {}),
                'weather': data.get('weather', []),
                'main': data.get('main', {}),
                'wind': data.get('wind', {}),
                'visibility': data.get('visibility', None),
                'name': data.get('name', None)
            }

            return useful_data
        else:
            print(f"Failed to get weather data for lat={lat}, lon={lon}")
            return {"error": "Failed to fetch data"}

# Example usage
weather_cache = WeatherCache()

# User input for city name
city = input("Enter the name of the city: ")
# Get the latitude and longitude for the chosen city
lat, lon = weather_cache.get_lat_long(city)
if lat is not None and lon is not None:
    print(f"Lat and Long for {city}: {lat}, {lon}")
    # Fetch weather data for the specified latitude and longitude
    weather_data = weather_cache.get_weather(lat, lon)
    # Print useful weather data
    print(f"Weather data for {city}:")
    print(f"Weather: {weather_data['weather']}")
    print(f"Main: {weather_data['main']}")
    print(f"Wind: {weather_data['wind']}")
    print(f"Visibility: {weather_data['visibility']}")
    print(f"City Name: {weather_data['name']}")
else:
    print(f"Failed to get lat and long for {city}.")
