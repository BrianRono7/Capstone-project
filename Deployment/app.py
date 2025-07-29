import streamlit as st
import pandas as pd
import numpy as np
import joblib
import gdown
import os

from predictor import recommend_crop_user_friendly, commodity_dict, market_dict, region_dict, county_dict

# ------------------ Data Load ------------------

# Google Drive CSV file setup
file_id = "146Y6-nKiuSnFoI8BKArR8153ZWvpnYgY"
url = f"https://drive.google.com/uc?id={file_id}"
output = "merged_data.csv"

# Download only if not already present
if not os.path.exists(output):
    st.info("📥 Downloading dataset...")
    try:
        gdown.download(url, output, quiet=False)
    except Exception as e:
        st.error(f"❌ Download failed: {e}")
        st.stop()

# Load the dataset
try:
    df = pd.read_csv(output)
    st.success("✅ Dataset loaded successfully!")
except Exception as e:
    st.error(f"❌ Failed to read the CSV file: {e}")
    st.stop()

# -------------- Header ----------------
st.set_page_config(page_title="🇰🇪 Food Price Prediction App", layout="wide")

st.title("🌾 Kenya Food Price Spike Early Warning System")
st.markdown("""
This intelligent system uses **machine learning and weather data** to forecast food prices across Kenyan markets.
""")

# -------------- Summary Dashboard ----------------
with st.container():
    st.subheader("📊 Dataset Summary")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Markets", df['market_x'].nunique())
    col2.metric("Commodities", df['commodity'].nunique())
    col3.metric("Regions", df['Region'].nunique())
    col4.metric("Counties", df['County'].nunique())

    st.dataframe(df.sample(5), use_container_width=True)

# -------------- Visuals ----------------
with st.container():
    st.subheader("🌧️ Average Rainfall by County")
    avg_rainfall = df.groupby('County')['rainfall_mm'].mean().sort_values(ascending=False)
    st.bar_chart(avg_rainfall)

    st.subheader("📈 Average Price by Commodity")
    avg_prices = df.groupby('commodity')['price'].mean().sort_values(ascending=False)
    st.bar_chart(avg_prices.head(10))

# -------------- Sidebar for Prediction ----------------
st.sidebar.header("📌 Predict Crop Price")

rainfall = st.sidebar.number_input("Rainfall (mm)", value=0.0)
month = st.sidebar.selectbox("Month", list(range(1, 13)), index=6)
year = st.sidebar.number_input("Year", value=2025)

commodity_name = st.sidebar.selectbox("Commodity", list(commodity_dict.keys()))
market_name = st.sidebar.selectbox("Market", list(market_dict.keys()))
region_name = st.sidebar.selectbox("Region", list(region_dict.keys()))
county_name = st.sidebar.selectbox("County", list(county_dict.keys()))

if st.sidebar.button("🚀 Predict Price"):
    prediction = recommend_crop_user_friendly(
        rainfall,
        month,
        year,
        commodity_name,
        market_name,
        region_name,
        county_name
    )
    st.sidebar.success(f"💰 Predicted Price: KES {prediction:.2f}")

# -------------- Current Conditions ----------------
with st.expander("📌 Current Rainfall & Market Prices (Sample)"):
    current = df.sort_values("date_x", ascending=False).head(10)
    st.dataframe(current[['commodity', 'market_x', 'County', 'rainfall_mm', 'price']], use_container_width=True)
