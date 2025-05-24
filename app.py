import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load model and preprocessor
def load_model():
    preprocessor = joblib.load("artifacts/preprocessor.pkl")
    model = joblib.load("artifacts/model.pkl")
    return preprocessor, model

# Make prediction
def make_prediction(preprocessor, model, input_data):
    transformed_data = preprocessor.transform(input_data)
    prediction = model.predict(transformed_data)
    return prediction

# Streamlit UI
st.set_page_config(page_title="Stock Price Predictor", layout="wide")

st.title("📈 Stock Price Predictor")
st.subheader("Predict future stock prices using machine learning")

with st.sidebar:
    st.header("User Input Features")
    ticker = st.text_input("Ticker Symbol", "AAPL")
    open_price = st.number_input("Open Price", value=150.0)
    high_price = st.number_input("High Price", value=153.0)
    low_price = st.number_input("Low Price", value=149.0)
    adj_close = st.number_input("Adjusted Close Price", value=152.0)
    volume = st.number_input("Volume", value=1000000)

    input_df = pd.DataFrame({
        'Ticker': [ticker],
        'Open': [open_price],
        'High': [high_price],
        'Low': [low_price],
        'Adj Close': [adj_close],
        'Volume': [volume]
    })

    if st.button("Predict"):
        preprocessor, model = load_model()
        prediction = make_prediction(preprocessor, model, input_df)

        st.success(f"Predicted Close Price: ${prediction[0]:.2f}")

        # Display prediction as a metric
        st.metric(label="📊 Predicted Price", value=f"${prediction[0]:.2f}", delta=f"{prediction[0] - adj_close:.2f}")

        # Line Chart Comparison
        st.subheader("📉 Price Comparison Chart")
        fig, ax = plt.subplots()
        ax.plot(['Adj Close', 'Predicted'], [adj_close, prediction[0]], marker='o')
        ax.set_ylabel("Price ($)")
        ax.set_title("Actual vs Predicted")
        st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit")
