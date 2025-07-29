import joblib
import numpy as np
from mappings import commodity_dict, market_dict, region_dict, county_dict

def recommend_crop_user_friendly(rainfall_mm, month, year, commodity, market, region, county):
    try:
        commodity_code = commodity_dict.get(commodity)
        market_code = market_dict.get(market)
        region_code = region_dict.get(region)
        county_code = county_dict.get(county)

        missing = []
        if commodity_code is None: missing.append("commodity")
        if market_code is None: missing.append("market")
        if region_code is None: missing.append("region")
        if county_code is None: missing.append("county")

        if missing:
            raise ValueError(f"Could not map: {', '.join(missing)}")

        try:
            model = joblib.load("best_model.pkl")
        except FileNotFoundError:
            raise FileNotFoundError("Model file 'best_model.pkl' not found.")

        X_new = np.array([[rainfall_mm, month, year, commodity_code, market_code, region_code, county_code]])
        prediction = model.predict(X_new)
        return prediction[0]

    except Exception as e:
        print(f"[ERROR] Prediction failed: {e}")
        return None
