import os
import joblib
import gdown
import numpy as np
from mappings import commodity_dict, market_dict, region_dict, county_dict

def recommend_crop_user_friendly(rainfall_mm, month, year, commodity, market, region, county):
    try:
        model_path = "best_model.pkl"
        file_id = "1RsWVLQ_LYXSfP0NUOaopUHAjCldXK69Y"
        url = f"https://drive.google.com/uc?id={file_id}"

        # ✅ Download model if not already present
        if not os.path.exists(model_path):
            print("📥 Downloading model from Google Drive...")
            gdown.download(url, model_path, quiet=False)

        # ✅ Confirm it was downloaded
        if not os.path.exists(model_path):
            raise FileNotFoundError("❌ Model download failed. 'best_model.pkl' not found.")

        # ✅ Load the model
        model = joblib.load(model_path)

        # ✅ Encode inputs
        commodity_code = commodity_dict.get(commodity)
        market_code = market_dict.get(market)
        region_code = region_dict.get(region)
        county_code = county_dict.get(county)

        if None in [commodity_code, market_code, region_code, county_code]:
            raise ValueError("Input mapping failed.")

        X_new = np.array([[rainfall_mm, month, year, commodity_code, market_code, region_code, county_code]])
        prediction = model.predict(X_new)
        return prediction[0]

    except Exception as e:
        print(f"❌ Model prediction error: {e}")
        return None
