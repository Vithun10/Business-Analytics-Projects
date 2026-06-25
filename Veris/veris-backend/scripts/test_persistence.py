import pandas as pd

from app.database import SessionLocal

from app.ml.fraud_engine import (
    FraudEngine
)

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

from app.services.persistence_service import (
    PersistenceService
)


print("\nLoading Dataset...")

df = pd.read_csv(
    "processed/feature_engineered.csv"
)

df = df.head(100)

print(
    f"Processing {len(df)} records"
)

# ----------------------------------
# Fraud
# ----------------------------------

fraud_scores = (
    FraudEngine()
    .score(df)
)

# ----------------------------------
# Credit
# ----------------------------------

credit_scores = (
    ProxyCreditEngine()
    .score(df)
)

credit_risks = (
    CreditEngine()
    .risk(
        credit_scores
    )
)

# ----------------------------------
# URS
# ----------------------------------

urs_scores = (
    UnifiedRiskService()
    .calculate(
        fraud_scores,
        credit_risks
    )
)

# ----------------------------------
# Decision
# ----------------------------------

decisions, tiers = (
    DecisionService()
    .evaluate(
        urs_scores
    )
)

# ----------------------------------
# Result DF
# ----------------------------------

df["FraudScore"] = fraud_scores
df["CreditScore"] = credit_scores
df["CreditRisk"] = credit_risks
df["URS"] = urs_scores
df["Decision"] = decisions
df["RiskTier"] = tiers

# ----------------------------------
# Save
# ----------------------------------

db = SessionLocal()

saved = (
    PersistenceService()
    .save_transactions(
        db,
        df
    )
)

print(
    f"\nSaved {saved} transactions"
)

db.close()