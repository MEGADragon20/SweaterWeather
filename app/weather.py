import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    r = requests.get(url, params=params, timeout=5)
    r.raise_for_status()
    print("r: ", r)
    data = r.json()

    return {
        "temp": data["main"]["temp"],
        "wind": data["wind"]["speed"],
        "rain": data.get("rain", {}).get("1h", 0)
    }
