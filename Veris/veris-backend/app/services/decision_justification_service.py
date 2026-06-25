class DecisionJustificationService:

    def generate(
        self,
        transaction
    ):

        reasons = []

        if transaction.fraud_score >= 0.30:

            reasons.append(
                "Elevated fraud probability detected"
            )

        if transaction.credit_risk >= 0.60:

            reasons.append(
                "High credit risk profile"
            )

        if (
            transaction.transaction_amount
            >= 10000
        ):

            reasons.append(
                "High transaction amount"
            )

        if (
            transaction.previous_transaction_count
            <= 2
        ):

            reasons.append(
                "Limited customer transaction history"
            )

        if not reasons:

            reasons.append(
                "No significant risk indicators detected"
            )

        return reasons