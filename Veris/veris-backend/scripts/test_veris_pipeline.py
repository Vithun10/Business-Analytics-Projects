import pandas as pd

from app.ml.fraud_engine import FraudEngine

from app.ml.proxy_credit_engine import (
    ProxyCreditEngine
)

from app.ml.credit_engine import (
    CreditEngine
)

from app.services.unified_risk_service import (
    UnifiedRiskService
)

from app.services.decision_service import (
    DecisionService
)


print("\nLoading Dataset...")

df = pd.read_csv(
    "processed/feature_engineered.csv"
)

df = df.sample(
    50000,random_state=42
)

print(
    f"Testing {len(df)} records"
)

# ----------------------------------
# Fraud
# ----------------------------------

fraud_engine = FraudEngine()

fraud_scores = fraud_engine.score(
    df
)

# ----------------------------------
# Credit
# ----------------------------------

proxy_engine = ProxyCreditEngine()

credit_scores = proxy_engine.score(
    df
)

credit_engine = CreditEngine()

credit_risks = credit_engine.risk(
    credit_scores
)

# ----------------------------------
# URS
# ----------------------------------

urs_service = UnifiedRiskService()

urs_scores = urs_service.calculate(
    fraud_scores,
    credit_risks
)

# ----------------------------------
# Decision
# ----------------------------------

decision_service = (
    DecisionService()
)

decisions, tiers = (
    decision_service.evaluate(
        urs_scores
    )
)

# ----------------------------------
# Results
# ----------------------------------

result_df = pd.DataFrame({

    "FraudScore":
        fraud_scores,

    "CreditScore":
        credit_scores,

    "CreditRisk":
        credit_risks,

    "URS":
        urs_scores,

    "Decision":
        decisions,

    "RiskTier":
        tiers
})

print(
    result_df
)

print(
    "\nDecision Counts"
)

print(
    result_df[
        "Decision"
    ].value_counts()
)