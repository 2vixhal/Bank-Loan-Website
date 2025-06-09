# predict.py

import joblib
import shap
import pandas as pd
import numpy as np
from risk_classifier import classify_risk


def load_model(model_path: str):
    return joblib.load(model_path)


def predict_and_explain(model, input_features: dict):
    """
    Predict loan approval, classify risk, and compute SHAP values.
    """
    # Ensure input DataFrame matches training features
    model_features = model.feature_names_in_
    input_df = pd.DataFrame([input_features])

    # Fill missing columns with 0, drop unknown columns
    for col in model_features:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[model_features]

    # Predict
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    risk = classify_risk(probability)

    # SHAP explainability
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(input_df)

    return {
        "prediction": int(prediction),
        "risk": risk,
        "shap_values": shap_values[1] if isinstance(shap_values, list) else shap_values
    }


if __name__ == "__main__":
    model_path = "best_model.pkl"
    model = load_model(model_path)

    # Input features: only supply user-filled or default fields
    input_features = {
        "no_of_dependents": 1,
        "income_annum": 700000,
        "loan_amount": 3000000,
        "loan_term": 120,
        "cibil_score": 160,
        "residential_assets_value": 500000,
        "commercial_assets_value": 0,
        "luxury_assets_value": 0,
        "bank_asset_value": 100000,
        "education_ Not Graduate": 0,
        "self_employed_ Yes": 1
    }

    result = predict_and_explain(model, input_features)
    print("Prediction:", result["prediction"])
    print("Risk Classification:", result["risk"])
    print("SHAP Values:", result["shap_values"])
