REQUIRED_COLUMNS = {

    "transaction_id",
    "customer_id",
    "transaction_amount",
    "merchant_category",
    "device_type",
    "device_id",
    "card_age_months",
    "previous_transaction_count",
    "billing_country",
    "shipping_country",
    "email_domain",
    "transaction_timestamp"
}


class UploadValidationService:

    def validate(
        self,
        dataframe
    ):

        uploaded_columns = set(
            dataframe.columns
        )

        missing_columns = (
            REQUIRED_COLUMNS
            -
            uploaded_columns
        )

        if missing_columns:

            return {

                "valid": False,

                "missing_columns":
                    list(
                        missing_columns
                    )
            }

        return {

            "valid": True,

            "missing_columns": []
        }