from app.repositories.transaction_repository import (
    TransactionRepository
)


class PersistenceService:

    def __init__(self):

        self.repository = (
            TransactionRepository()
        )

    def save_transactions(
        self,
        db,
        dataframe
    ):

        transactions = []

        for _, row in dataframe.iterrows():

            transactions.append({

    "transaction_id":
        str(
            row.get(
                "transaction_id",
                row.get(
                    "TransactionID",
                    "UNKNOWN"
                )
            )
        ),

    "customer_id":
        str(
            row.get(
                "customer_id",
                row.get(
                    "card1",
                    "UNKNOWN"
                )
            )
        ),

    "transaction_amount":
        float(
            row.get(
                "transaction_amount",
                row.get(
                    "TransactionAmt",
                    0
                )
            )
        ),

    "merchant_category":
        str(
            row.get(
                "merchant_category",
                "UNKNOWN"
            )
        ),

    "device_type":
        str(
            row.get(
                "device_type",
                row.get(
                    "DeviceType",
                    "UNKNOWN"
                )
            )
        ),

    "email_domain_type":
        str(
            row.get(
                "email_domain_type",
                "UNKNOWN"
            )
        ),

    "previous_transaction_count":
        int(
            row.get(
                "previous_transaction_count",
                0
            )
        ),

    "fraud_score":
        float(
            row["FraudScore"]
        ),

    "credit_score":
        float(
            row["CreditScore"]
        ),

    "credit_risk":
        float(
            row["CreditRisk"]
        ),

    "unified_risk_score":
        float(
            row["URS"]
        ),

    "risk_tier":
        row["RiskTier"],

    "decision":
        row["Decision"]
})

        self.repository.bulk_create(
            db,
            transactions
        )

        return len(transactions)