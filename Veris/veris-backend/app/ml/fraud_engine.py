import joblib
import pandas as pd
from app.ml.model_loader import load_rf_model

VERIS_FRAUD_FEATURES = [

    "TransactionAmt",

    "hour_of_day",

    "identity_consistency",

    "device_consistency",

    "address_consistency",

    "previous_transaction_count",

    "card_age_months",

    "missingness_quality"
]


class FraudEngine:

    def __init__(self):

        self.rf_model = load_rf_model()

        self.xgb_model = joblib.load(
        "app/ml/artifacts/veris_fraud_xgb.pkl"
)

    def score(
        self,
        feature_df: pd.DataFrame
    ):

        X = feature_df[VERIS_FRAUD_FEATURES].fillna(0)

        rf_prob = (
            self.rf_model
            .predict_proba(X)[:, 1]
        )

        xgb_prob = (
            self.xgb_model
            .predict_proba(X)[:, 1]
        )

        fraud_score = (
            0.9 * rf_prob
            + 0.1 * xgb_prob
        )

        return fraud_score