import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
import joblib
from imblearn.over_sampling import SMOTE

# Load and preprocess data
def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)

    if 'cibil_score' in data.columns:
        data['cibil_score'] = data['cibil_score'].fillna(data['cibil_score'].median())

    if 'loan_status' in data.columns:
        print("\n🔍 Unique values in raw 'loan_status' column BEFORE mapping:")
        print(data['loan_status'].unique())

        data = data[data['loan_status'].notna()]  # Drop NaNs

        # Only map if data is in string format
        if data['loan_status'].dtype == object:
            data['loan_status'] = data['loan_status'].str.lower().str.strip()
            data['loan_status'] = data['loan_status'].map({'approved': 1, 'rejected': 0})

        print("\n✅ Value counts after possible mapping:")
        print(data['loan_status'].value_counts())

    data.fillna(0, inplace=True)

    if 'education' in data.columns and 'self_employed' in data.columns:
        data = pd.get_dummies(data, columns=['education', 'self_employed'], drop_first=True)

    if 'loan_id' in data.columns:
        data.drop(['loan_id'], axis=1, inplace=True)

    return data

# Train and evaluate models
def train_and_evaluate(X_train, X_test, y_train, y_test):
    models = {
        "RandomForest": RandomForestClassifier(),
        "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='logloss'),
        "LogisticRegression": LogisticRegression(max_iter=1000)
    }
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]
        results[name] = {
            "model": model,
            "accuracy": accuracy_score(y_test, y_pred),
            "f1": f1_score(y_test, y_pred),
            "roc_auc": roc_auc_score(y_test, y_prob)
        }
    return results

# Hyperparameter tuning
def tune_model(model, param_grid, X_train, y_train):
    grid_search = GridSearchCV(model, param_grid, cv=3, scoring='roc_auc')
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_

# Main training pipeline
def main():
    data = load_and_preprocess_data("loan_approval_dataset.csv")

    # Count total number of rows for each class
    print("\n🔎 Total counts before splitting:")
    print(f"Rows with loan_status = 1 (Approved): {sum(data['loan_status'] == 1)}")
    print(f"Rows with loan_status = 0 (Rejected): {sum(data['loan_status'] == 0)}")

    if data["loan_status"].isna().sum() > 0:
        raise ValueError("Target column 'loan_status' contains NaN values after preprocessing.")

    X = data.drop("loan_status", axis=1)
    y = data["loan_status"]

    # Try different test sizes
    for test_ratio in [0.2, 0.1, 0.05]:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_ratio, stratify=y, random_state=42
        )
        if len(y_train.unique()) == 2:
            print(f"\n✅ Both classes present in training data with test_size={test_ratio}")
            break
        print(f"\n⚠️ Only one class in training data with test_size={test_ratio}, retrying...")

    if len(y_train.unique()) < 2:
        raise ValueError("❌ Training data still contains only one class. Not enough data for both 0 and 1 labels.")

    print("\n✅ y_train distribution before SMOTE:")
    print(y_train.value_counts())
    print("✅ y_test distribution:")
    print(y_test.value_counts())

    print("\n📈 Applying SMOTE...")
    smote = SMOTE(random_state=42)
    X_train, y_train = smote.fit_resample(X_train, y_train)

    print("✅ y_train distribution after SMOTE:")
    print(y_train.value_counts())

    results = train_and_evaluate(X_train, X_test, y_train, y_test)
    best_model_name = max(results, key=lambda x: results[x]["roc_auc"])
    best_model = results[best_model_name]["model"]

    if best_model_name == "RandomForest":
        param_grid = {"n_estimators": [100, 200], "max_depth": [10, 20, None]}
    elif best_model_name == "XGBoost":
        param_grid = {"n_estimators": [100, 200], "learning_rate": [0.01, 0.1]}
    else:
        param_grid = {"C": [0.1, 1, 10]}

    tuned_model = tune_model(best_model, param_grid, X_train, y_train)
    joblib.dump(tuned_model, "best_model.pkl")
    print(f"\n✅ Best model ({best_model_name}) saved as 'best_model.pkl'.")

if __name__ == "__main__":
    main()
