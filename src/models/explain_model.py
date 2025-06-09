# explain_model.py

import joblib
import shap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_model(model_path: str):
    return joblib.load(model_path)


def generate_shap_summary(model, X: pd.DataFrame, output_path: str = None):
    """
    Generate a SHAP summary plot for the given model and dataset.
    """
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)

    shap.summary_plot(shap_values, X, show=output_path is None)

    if output_path:
        plt.savefig(output_path)
        plt.close()


def generate_shap_force_plot(model, X: pd.DataFrame, instance_idx: int, output_path: str = None):
    """
    Generate a SHAP force plot for a single prediction.
    """
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)

    shap.force_plot(
        explainer.expected_value[1] if isinstance(shap_values, list) else explainer.expected_value,
        shap_values[1][instance_idx] if isinstance(shap_values, list) else shap_values[instance_idx],
        X.iloc[instance_idx],
        matplotlib=True,
        show=output_path is None
    )

    if output_path:
        plt.savefig(output_path)
        plt.close()


if __name__ == "__main__":
    model_path = "best_model.pkl"
    data_path = "loan_approval_dataset.csv"

    model = load_model(model_path)
    data = pd.read_csv(data_path)

    # Preprocess
    if 'cibil_score' in data.columns:
        data['cibil_score'] = data['cibil_score'].fillna(data['cibil_score'].median())

    data.fillna(0, inplace=True)

    if 'loan_status' in data.columns and data['loan_status'].dtype == object:
        data['loan_status'] = data['loan_status'].str.lower().str.strip()
        data['loan_status'] = data['loan_status'].map({'approved': 1, 'rejected': 0})

    if 'education' in data.columns and 'self_employed' in data.columns:
        data = pd.get_dummies(data, columns=['education', 'self_employed'], drop_first=True)

    X = data.drop(columns=[col for col in ['loan_status', 'loan_id'] if col in data.columns])

    # Generate SHAP plots
    generate_shap_summary(model, X, output_path="shap_summary.png")
    print("SHAP summary plot saved as 'shap_summary.png'.")

    instance_idx = 0
    generate_shap_force_plot(model, X, instance_idx, output_path="shap_force_plot.png")
    print(f"SHAP force plot for instance {instance_idx} saved as 'shap_force_plot.png'.")
