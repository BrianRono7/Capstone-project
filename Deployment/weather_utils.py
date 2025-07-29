import requests

def get_weather_by_city(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},KE&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": city,
            "temp": data["main"]["temp"],
            "condition": data["weather"][0]["description"],
            "lat": data["coord"]["lat"],
            "lon": data["coord"]["lon"]
        }
        return weather
    else:
        return None
