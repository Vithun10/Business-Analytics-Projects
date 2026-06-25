class UnifiedRiskService:

    def calculate(
        self,
        fraud_score,
        credit_risk
    ):

        urs = (
            0.6 * fraud_score
            +
            0.4 * credit_risk
        )

        return urs