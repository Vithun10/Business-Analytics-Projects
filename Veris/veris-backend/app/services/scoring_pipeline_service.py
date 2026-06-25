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

        fraud_scores = (
            FraudEngine()
            .score(df)
        )

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

        urs_scores = (
            UnifiedRiskService()
            .calculate(
                fraud_scores,
                credit_risks
            )
        )

        decisions, tiers = (
            DecisionService()
            .evaluate(
                urs_scores
            )
        )

        df["FraudScore"] = (
            fraud_scores
        )

        df["CreditScore"] = (
            credit_scores
        )

        df["CreditRisk"] = (
            credit_risks
        )

        df["URS"] = (
            urs_scores
        )

        df["Decision"] = (
            decisions
        )

        df["RiskTier"] = (
            tiers
        )

        return df