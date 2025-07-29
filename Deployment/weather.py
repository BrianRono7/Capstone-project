# weather.py
import requests
import streamlit as st

API_KEY = st.secrets["weather"]["api_key"]
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_forecasted_rainfall(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return 0.0

    data = response.json()
    
    # Return rainfall from next 3-hour forecast (if any)
    for forecast in data["list"]:
        rain = forecast.get("rain", {}).get("3h", 0.0)
        return rain

    return 0.0
