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


class ScoringPipelineService:
 def score(
    self,
    df: pd.DataFrame
):

    print("=" * 60)
    print("STEP 1: Creating FraudEngine")
    fraud_engine = FraudEngine()

    print("STEP 2: Scoring fraud")
    fraud_scores = fraud_engine.score(df)

    print("STEP 3: Creating ProxyCreditEngine")
    proxy = ProxyCreditEngine()

    print("STEP 4: Credit scoring")
    credit_scores = proxy.score(df)

    print("STEP 5: Credit risk")
    credit_risks = CreditEngine().risk(
        credit_scores
    )

    print("STEP 6: Unified Risk")
    urs_scores = UnifiedRiskService().calculate(
        fraud_scores,
        credit_risks
    )

    print("STEP 7: Decision")
    decisions, tiers = DecisionService().evaluate(
        urs_scores
    )

    print("STEP 8: Writing results")
    df["FraudScore"] = fraud_scores
    df["CreditScore"] = credit_scores
    df["CreditRisk"] = credit_risks
    df["URS"] = urs_scores
    df["Decision"] = decisions
    df["RiskTier"] = tiers

    print("STEP 9: Completed Successfully")
    print("=" * 60)

    return df
    
    