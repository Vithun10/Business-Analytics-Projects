import pandas as pd

from app.ml.proxy_credit_engine import ProxyCreditEngine
from app.ml.credit_engine import CreditEngine


print("\nLoading Dataset...")

df = pd.read_csv(
    "processed/feature_engineered.csv"
)

print(
    f"Dataset Shape: {df.shape}"
)

print("\nGenerating Credit Scores...")

proxy_engine = ProxyCreditEngine()

credit_scores = proxy_engine.score(df)

print("\nGenerating Credit Risks...")

risk_engine = CreditEngine()

credit_risks = risk_engine.risk(
    credit_scores
)

print("\n========== CREDIT SCORE SUMMARY ==========")

print(
    credit_scores.describe()
)

print("\n========== CREDIT RISK SUMMARY ==========")

print(
    credit_risks.describe()
)

print(
    "\nAverage Credit Score:",
    round(
        credit_scores.mean(),
        4
    )
)

print(
    "Average Credit Risk:",
    round(
        credit_risks.mean(),
        4
    )
)

print("\nTop 10 Credit Scores")

print(
    credit_scores.head(10)
)

print("\nTop 10 Credit Risks")

print(
    credit_risks.head(10)
)