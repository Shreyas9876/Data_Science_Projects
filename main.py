import os
import sys
import numpy as np

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException


def run_pipeline():
    try:
        print("🔹 Step 1: Data Ingestion")
        ingestion = DataIngestion()
        train_path, test_path = ingestion.initiate_data_ingestion()
        print(f"✅ Data Ingested: \nTrain: {train_path} \nTest: {test_path}")

        print("\n🔹 Step 2: Data Transformation")
        transformer = DataTransformation()
        X_train, X_test, y_train, y_test = transformer.initiate_data_transformation(train_path, test_path)
        print("✅ Data Transformed")

        print("\n🔹 Step 3: Model Training")
        trainer = ModelTrainer()

        # Combine features and labels into arrays
        train_array = np.c_[X_train, y_train]
        test_array = np.c_[X_test, y_test]

        results = trainer.initiate_model_trainer(train_array, test_array)
        print("✅ Model Training Completed")
        print("📊 Evaluation Metrics (R2 Score):", results)

    except CustomException as ce:
        print("❌ Custom Exception occurred:", ce)
    except Exception as e:
        print("❌ Unexpected Error:", e)


if __name__ == "__main__":
    run_pipeline()
