import joblib
import pandas as pd

def load_objects(preprocessor_path="artifacts/preprocessor.pkl",
                 model_path="artifacts/model.pkl"):
    print("Loading preprocessor and model...")
    preprocessor = joblib.load(preprocessor_path)
    model = joblib.load(model_path)
    print("Loaded successfully.")
    return preprocessor, model

def predict_sample(preprocessor, model):
    columns = ['Ticker', 'Open', 'High', 'Low', 'Adj Close', 'Volume']
    sample_data = pd.DataFrame([["AAPL", 150.0, 153.0, 149.0, 152.0, 1000000]], columns=columns)
    print("Sample input:\n", sample_data)
    transformed_data = preprocessor.transform(sample_data)
    prediction = model.predict(transformed_data)
    print("Prediction:", prediction)

def predict_full_dataset(preprocessor, model, input_path="artifacts/data.csv", output_path="artifacts/predictions.csv"):
    print(f"Loading full dataset from {input_path}...")
    data = pd.read_csv(input_path)
    
    print("Transforming data...")
    X = preprocessor.transform(data)
    
    print("Making predictions...")
    data['Prediction'] = model.predict(X)
    
    print(f"Saving predictions to {output_path}...")
    data.to_csv(output_path, index=False)
    print("Predictions saved successfully.")

if __name__ == "__main__":
    preprocessor, model = load_objects()
    predict_sample(preprocessor, model)         # existing sample prediction
    predict_full_dataset(preprocessor, model)   # new full dataset prediction and save
