class ShapEngine:

    def explain(
        self,
        transaction
    ):

        features = []

        if transaction.fraud_score > 0.25:

            features.append({

                "feature":
                "Fraud Score",

                "impact":
                round(
                    transaction.fraud_score,
                    4
                )
            })

        if transaction.credit_risk > 0.40:

            features.append({

                "feature":
                "Credit Risk",

                "impact":
                round(
                    transaction.credit_risk,
                    4
                )
            })

        if transaction.transaction_amount > 10000:

            features.append({

                "feature":
                "Transaction Amount",

                "impact":
                0.10
            })

        return {

            "feature_contributions":
            features
        }