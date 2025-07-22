# predictor.py

import joblib
import numpy as np
from mappings import commodity_dict, market_dict, region_dict, county_dict


# Load mappings (replace these with your actual mappings or import from a separate module)


def recommend_crop_user_friendly(rainfall_mm, month, year, commodity, market, region, county):
    # Map names to codes
    commodity_code = commodity_dict.get(commodity)
    market_code = market_dict.get(market)
    region_code = region_dict.get(region)
    county_code = county_dict.get(county)

    if None in [commodity_code, market_code, region_code, county_code]:
        raise ValueError("One or more inputs could not be mapped to codes.")

    # Load model
    model = joblib.load("best_model.pkl")

    # Create input array
    X_new = np.array([[rainfall_mm, month, year, commodity_code, market_code, region_code, county_code]])

    # Predict and return price
    prediction = model.predict(X_new)
    return prediction[0]
