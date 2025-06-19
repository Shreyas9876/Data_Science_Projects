import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# 🔁 Required imports for loading the joblib files
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from xgboost import XGBRegressor  # Replace with the correct model if different

# 📂 Load model and preprocessor
def load_model():
    try:
        preprocessor = joblib.load("artifacts/preprocessor.pkl")
        model = joblib.load("artifacts/model.pkl")
        return preprocessor, model
    except FileNotFoundError:
        st.error("❌ Model or preprocessor file not found. Please train the model first.")
        st.stop()
    except Exception as e:
        st.error(f"❌ Failed to load model: {str(e)}")
        st.stop()

# 🧠 Make prediction
def predict(preprocessor, model, input_df):
    processed_data = preprocessor.transform(input_df)
    prediction = model.predict(processed_data)
    return prediction

# 🎯 Streamlit UI
def main():
    st.title("📈 Stock Price Predictor")

    st.markdown("""
    Enter the stock data below to predict the future closing price.
    """)

    # Replace these with your actual input features
    open_price = st.number_input("Open Price", min_value=0.0, value=100.0)
    high_price = st.number_input("High Price", min_value=0.0, value=105.0)
    low_price = st.number_input("Low Price", min_value=0.0, value=95.0)
    volume = st.number_input("Volume", min_value=0.0, value=1_000_000.0)

    input_data = {
        "Open": [open_price],
        "High": [high_price],
        "Low": [low_price],
        "Volume": [volume]
    }

    input_df = pd.DataFrame(input_data)

    if st.button("Predict Closing Price"):
        preprocessor, model = load_model()
        prediction = predict(preprocessor, model, input_df)
        st.success(f"📊 Predicted Closing Price: ₹{prediction[0]:,.2f}")

if __name__ == "__main__":
    main()
