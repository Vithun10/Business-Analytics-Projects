import os
import joblib
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    roc_auc_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)

from xgboost import XGBClassifier


# =====================================================
# CONFIG
# =====================================================

DATA_PATH = "processed/feature_engineered.csv"

RF_MODEL_PATH = "app/ml/artifacts/fraud_rf.pkl"
XGB_MODEL_PATH = "app/ml/artifacts/fraud_xgb.pkl"

FRAUD_FEATURES = [
    "TransactionAmt",
    "hour_of_day",
    "card1",
    "card2",
    "card3",
    "card5",
    "addr1",
    "addr2",
    "identity_consistency",
    "device_consistency",
    "missingness_quality",
    "previous_transaction_count",
]

TARGET = "isFraud"

THRESHOLDS = [0.50, 0.30, 0.20, 0.10]


# =====================================================
# HELPER
# =====================================================

def evaluate_model(name, y_true, probabilities):

    print("\n" + "=" * 70)
    print(name)
    print("=" * 70)

    auc = roc_auc_score(y_true, probabilities)

    print(f"ROC-AUC: {auc:.4f}")

    best_f1 = 0
    best_threshold = 0.5

    for threshold in THRESHOLDS:

        predictions = (
            probabilities >= threshold
        ).astype(int)

        precision = precision_score(
            y_true,
            predictions,
            zero_division=0
        )

        recall = recall_score(
            y_true,
            predictions,
            zero_division=0
        )

        f1 = f1_score(
            y_true,
            predictions,
            zero_division=0
        )

        print(
            f"\nThreshold={threshold}"
        )
        print(
            f"Precision={precision:.4f}"
        )
        print(
            f"Recall={recall:.4f}"
        )
        print(
            f"F1={f1:.4f}"
        )

        if f1 > best_f1:
            best_f1 = f1
            best_threshold = threshold

    print("\nBest Threshold:", best_threshold)
    print("Best F1:", round(best_f1, 4))

    predictions = (
        probabilities >= best_threshold
    ).astype(int)

    cm = confusion_matrix(
        y_true,
        predictions
    )

    print("\nConfusion Matrix")
    print(cm)

    return best_threshold


# =====================================================
# LOAD DATA
# =====================================================

print("\nLoading Dataset...")

df = pd.read_csv(DATA_PATH)

print("Dataset Shape:", df.shape)

# Development mode
# Uncomment if needed

# df = df.sample(
#     100000,
#     random_state=42
# )

df = df[FRAUD_FEATURES + [TARGET]]

df = df.fillna(0)

X = df[FRAUD_FEATURES]
y = df[TARGET]

# =====================================================
# TRAIN TEST SPLIT
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTrain Shape:", X_train.shape)
print("Test Shape :", X_test.shape)

# =====================================================
# CLASS IMBALANCE
# =====================================================

fraud_count = y_train.sum()

non_fraud_count = (
    len(y_train) - fraud_count
)

scale_pos_weight = (
    non_fraud_count / fraud_count
)

print(
    "\nscale_pos_weight:",
    round(scale_pos_weight, 2)
)

# =====================================================
# RANDOM FOREST
# =====================================================

print("\nTraining Random Forest...")

rf_model = RandomForestClassifier(
    n_estimators=300,
    max_depth=15,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)

rf_model.fit(
    X_train,
    y_train
)

rf_prob = rf_model.predict_proba(
    X_test
)[:, 1]

rf_best_threshold = evaluate_model(
    "RANDOM FOREST",
    y_test,
    rf_prob
)

# =====================================================
# XGBOOST
# =====================================================

print("\nTraining XGBoost...")

xgb_model = XGBClassifier(
    n_estimators=300,
    max_depth=8,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    scale_pos_weight=scale_pos_weight,
    random_state=42,
    eval_metric="logloss"
)

xgb_model.fit(
    X_train,
    y_train
)

xgb_prob = xgb_model.predict_proba(
    X_test
)[:, 1]

xgb_best_threshold = evaluate_model(
    "XGBOOST",
    y_test,
    xgb_prob
)

# =====================================================
# SAVE MODELS
# =====================================================

os.makedirs(
    "app/ml/artifacts",
    exist_ok=True
)

joblib.dump(
    rf_model,
    RF_MODEL_PATH
)

joblib.dump(
    xgb_model,
    XGB_MODEL_PATH
)

print("\nModels Saved")
print(RF_MODEL_PATH)
print(XGB_MODEL_PATH)

print("\nBest RF Threshold:", rf_best_threshold)
print("Best XGB Threshold:", xgb_best_threshold)