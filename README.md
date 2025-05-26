Title: Stock Price Prediction Using Machine Learning

Project URL: https://shreyas9876-data-science-projects-app-a5zelz.streamlit.app/

GitHub Repository: https://github.com/Shreyas9876/Data_Science_Projects.git

Overview

This project aims to predict stock prices based on historical data using machine learning techniques. The model is deployed as an interactive Streamlit web application that allows users to input stock parameters and get predictions.

Problem Statement

Stock price prediction is crucial for investors and analysts. By leveraging past stock data, we aim to build a model that can predict the next adjusted close price, helping in decision-making and trend analysis.

Tools & Technologies

Language: Python

Libraries: pandas, scikit-learn, joblib, matplotlib, seaborn, streamlit

Model: Linear Regression (can be upgraded to XGBoost, LSTM, etc.)

Deployment: Streamlit

Version Control: Git & GitHub

Workflow

Data Collection:

Used historical stock data from CSV files.

Data Preprocessing (data_ingestion.py):

Cleaned null values

Formatted data types

Selected relevant features

Exploratory Data Analysis (EDA):

Plotted closing price trends

Analyzed correlation heatmaps

Feature Engineering & Preprocessing:

Encoded categorical data (Ticker)

Normalized numerical features

Model Training:

Trained a linear regression model

Evaluated with RMSE and R2 score

Model Saving:

Serialized using joblib (model.pkl, preprocessor.pkl)

Prediction (predict.py):

Loaded model & preprocessor

Made predictions on sample input

Exported to predictions.csv

Visualization:

Imported prediction.csv into Power BI

Created line charts, bar graphs, tables, and key influencers

Deployment (app.py):

Built interactive web UI using Streamlit

Displayed prediction results based on user input

Project Deployment:

Hosted on Streamlit Cloud

Project Structure

Data_Science_Projects/
├── artifacts/
│   ├── data.csv
│   ├── model.pkl
│   └── preprocessor.pkl
├── app.py
├── predict.py
├── data_ingestion.py
├── requirements.txt
├── setup.py
└── README.md

How to Run Locally

# Clone the repository
git clone https://github.com/Shreyas9876/Data_Science_Projects.git
cd Data_Science_Projects

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

Future Enhancements

Add LSTM/XGBoost models for better accuracy

Integrate real-time stock data APIs

Enable user login for personalized dashboards

Track prediction history

License

This project is open-source and free to use for learning and academic purposes.

