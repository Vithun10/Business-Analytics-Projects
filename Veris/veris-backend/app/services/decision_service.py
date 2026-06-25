class DecisionService:

    def evaluate(
        self,
        urs
    ):

        decisions = []

        risk_tiers = []

        for score in urs:

            if score < 0.15:

                decisions.append(
                    "APPROVE"
                )

                risk_tiers.append(
                    "LOW"
                )

            elif score <= 0.22:

                decisions.append(
                    "REVIEW"
                )

                risk_tiers.append(
                    "MEDIUM"
                )

            else:

                decisions.append(
                    "DECLINE"
                )

                risk_tiers.append(
                    "HIGH"
                )

        return (
            decisions,
            risk_tiers
        )