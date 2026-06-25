class AIRiskAnalystService:

    def analyze(
        self,
        transaction,
        reasons
    ):

        decision = transaction.decision

        if decision == "APPROVE":

            recommendation = (
                "Transaction may be approved automatically."
            )

        elif decision == "REVIEW":

            recommendation = (
                "Manual analyst review is recommended."
            )

        else:

            recommendation = (
                "Transaction should be declined and investigated."
            )

        summary = (
             f"Transaction {transaction.transaction_id} "
             f"was classified as {transaction.risk_tier} risk. "
             f"Fraud Score={transaction.fraud_score:.3f}, "
             f"Credit Risk={transaction.credit_risk:.3f}, "
             f"URS={transaction.unified_risk_score:.3f}. "
             f"Key findings include: {', '.join(reasons)}."
        )

        return {

            "summary":
                summary,

            "recommendation":
                recommendation,

            "risk_level":
                transaction.risk_tier,

            "decision":
                transaction.decision
        }