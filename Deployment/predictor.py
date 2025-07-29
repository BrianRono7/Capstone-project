import os
import joblib
import gdown
import numpy as np
from mappings import commodity_dict, market_dict, region_dict, county_dict

def recommend_crop_user_friendly(rainfall_mm, month, year, commodity, market, region, county):
    try:
        # ✅ Google Drive Model Link
        model_path = "best_model.pkl"
        file_id = "1RsWVLQ_LYXSfP0NUOaopUHAjCldXK69Y"
        url = f"https://drive.google.com/uc?id={file_id}"

        # Download the model if not already available
        if not os.path.exists(model_path):
            gdown.download(url, model_path, quiet=False)

        # Load the model
        model = joblib.load(model_path)

        # Map user-friendly names to encoded integers
        commodity_code = commodity_dict.get(commodity)
        market_code = market_dict.get(market)
        region_code = region_dict.get(region)
        county_code = county_dict.get(county)

        if None in [commodity_code, market_code, region_code, county_code]:
            raise ValueError("One or more inputs could not be mapped to codes.")

        # Format input for prediction
        X_new = np.array([[rainfall_mm, month, year, commodity_code, market_code, region_code, county_code]])

        # Predict price
        prediction = model.predict(X_new)
        return prediction[0]

    except Exception as e:
        print(f"❌ Prediction error: {e}")
        return None
