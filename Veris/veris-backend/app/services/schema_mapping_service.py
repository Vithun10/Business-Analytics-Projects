import pandas as pd


class SchemaMappingService:

    def transform(
        self,
        df: pd.DataFrame
    ):

        working_df = df.copy()

        # -----------------------
        # Fraud Features
        # -----------------------

        working_df["TransactionAmt"] = (
            working_df[
                "transaction_amount"
            ]
        )

        working_df["DeviceType"] = (
            working_df[
                "device_type"
            ]
        )

        # -----------------------
        # Proxy Features
        # -----------------------

        working_df[
            "device_consistency"
        ] = (
            working_df[
                "device_id"
            ]
            .notna()
            .astype(int)
        )

        working_df[
            "identity_consistency"
        ] = 1

        working_df[
            "address_consistency"
        ] = (
            (
                working_df[
                    "billing_country"
                ]
                ==
                working_df[
                    "shipping_country"
                ]
            )
            .astype(int)
        )

        working_df[
            "missingness_quality"
        ] = 1

        working_df["hour_of_day"] = (
            pd.to_datetime(
                working_df["transaction_timestamp"]
            ).dt.hour
        )

        return working_df