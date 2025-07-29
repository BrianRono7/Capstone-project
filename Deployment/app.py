import streamlit as st
import pandas as pd
import numpy as np
import gdown
import os
import json
import folium
from streamlit_folium import st_folium

from predictor import recommend_crop_user_friendly
from mappings import (
    commodity_dict, market_dict, region_dict, county_dict, county_to_city
)
from weather import get_forecasted_rainfall

# ---------------------- CONFIGURATION ----------------------

st.set_page_config(
    page_title="🇰🇪 Kenya Food Price Spike Early Warning System",
    layout="wide"
)

# ---------------------- TITLE ----------------------

st.title("🌾 Kenya Food Price Spike Early Warning System")
st.markdown("""
This intelligent dashboard leverages **machine learning** and **real-time weather data** to forecast food prices across Kenyan markets.
""")

# ---------------------- LOAD DATASET ----------------------

file_id = "146Y6-nKiuSnFoI8BKArR8153ZWvpnYgY"
url = f"https://drive.google.com/uc?id={file_id}"
output = "merged_data.csv"

if not os.path.exists(output):
    st.info("📥 Downloading dataset...")
    try:
        gdown.download(url, output, quiet=False)
    except Exception as e:
        st.error(f"❌ Download failed: {e}")
        st.stop()

try:
    df = pd.read_csv(output)
    st.success("✅ Dataset loaded successfully!")
except Exception as e:
    st.error(f"❌ Failed to read the CSV file: {e}")
    st.stop()

# ---------------------- DATA SUMMARY ----------------------

with st.container():
    st.subheader("📊 Dataset Overview")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🛒 Markets", df['market_x'].nunique())
    col2.metric("🌽 Commodities", df['commodity'].nunique())
    col3.metric("🗺️ Regions", df['Region'].nunique())
    col4.metric("🏛 Counties", df['County'].nunique())

    st.markdown("### 🔍 Sample of Dataset")
    st.dataframe(df.sample(5), use_container_width=True)

# ---------------------- VISUALIZATIONS ----------------------

with st.container():
    st.subheader("🌧️ Average Rainfall by County")
    avg_rainfall = df.groupby('County')['rainfall_mm'].mean().sort_values(ascending=False)
    st.bar_chart(avg_rainfall)

    st.subheader("📈 Average Price by Commodity")
    avg_prices = df.groupby('commodity')['price'].mean().sort_values(ascending=False)
    st.bar_chart(avg_prices.head(10))

# ---------------------- SIDEBAR – PREDICTION INPUTS ----------------------

st.sidebar.header("📌 Food Price Prediction")

month = st.sidebar.selectbox("📅 Month", list(range(1, 13)), index=6)
year = st.sidebar.number_input("📆 Year", value=2025)

commodity_name = st.sidebar.selectbox("🌾 Commodity", list(commodity_dict.keys()))
market_name = st.sidebar.selectbox("🏪 Market", list(market_dict.keys()))
region_name = st.sidebar.selectbox("🗺️ Region", list(region_dict.keys()))
county_name = st.sidebar.selectbox("🏛 County", list(county_dict.keys()))

# ---------------------- AUTOMATED WEATHER FORECAST ----------------------

city = county_to_city.get(county_name)
rainfall = 0.0

if city:
    st.sidebar.info(f"📡 Getting forecasted rainfall for **{city}**...")
    try:
        rainfall = get_forecasted_rainfall(city)
        st.sidebar.success(f"🌧️ Forecasted Rainfall: {rainfall:.2f} mm")
    except Exception as e:
        st.sidebar.warning(f"⚠️ Failed to fetch rainfall: {e}")
else:
    st.sidebar.warning("⚠️ No city mapping found. Using 0 mm rainfall.")

# ---------------------- PREDICTION OUTPUT ----------------------

if st.sidebar.button("🚀 Predict Price"):
    try:
        prediction = recommend_crop_user_friendly(
            rainfall, month, year,
            commodity_name, market_name,
            region_name, county_name
        )
        if prediction is not None:
            st.sidebar.success(f"💰 Predicted Price: KES {prediction:.2f}")
        else:
            st.sidebar.warning("⚠️ Prediction failed. Check your input or model.")
    except Exception as e:
        st.sidebar.error(f"❌ Error: {e}")

# ---------------------- CURRENT SNAPSHOT ----------------------

with st.expander("📌 Current Rainfall & Market Prices (Sample)"):
    current = df.sort_values("date_x", ascending=False).head(10)
    st.dataframe(current[['commodity', 'market_x', 'County', 'rainfall_mm', 'price']], use_container_width=True)

# ---------------------- FORECAST MAP ----------------------

st.subheader("🗺️ Kenya Forecast Rainfall Map")

try:
    with open("kenya_counties.geojson", "r") as f:
        geojson_data = json.load(f)

    # Fetch rainfall per county from OpenWeather API
    forecast_data = {
        county: get_forecasted_rainfall(city)
        for county, city in county_to_city.items()
    }

    forecast_df = pd.DataFrame(forecast_data.items(), columns=["County", "Rainfall"])

    # Create folium map
    m = folium.Map(location=[0.0236, 37.9062], zoom_start=6)

    folium.Choropleth(
        geo_data=geojson_data,
        data=forecast_df,
        columns=["County", "Rainfall"],
        key_on="feature.properties.COUNTY",
        fill_color="YlGnBu",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Forecast Rainfall (mm)",
    ).add_to(m)

    st_folium(m, width=800, height=600)

except Exception as e:
    st.error(f"❌ Could not render Kenya map: {e}")
