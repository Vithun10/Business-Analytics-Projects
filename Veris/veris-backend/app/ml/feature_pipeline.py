import pandas as pd
import numpy as np


class FeaturePipeline:

    def transform(self, df: pd.DataFrame):


        # Time features
        df["hour_of_day"] = (df["TransactionDT"] // 3600) % 24

        # Email domain type
        consumer_domains = [
            "gmail.com",
            "yahoo.com",
            "hotmail.com",
            "outlook.com"
        ]

        df["email_domain_type"] = np.where(
            df["P_emaildomain"].isin(consumer_domains),
            "consumer",
            "business"
        )

        # Missing device
        df["missing_device_flag"] = (
            df["DeviceType"]
            .isna()
            .astype(int)
        )

        # Identity consistency
        identity_cols = [
            c for c in df.columns
            if c.startswith("id_")
        ]

        if identity_cols:
            df["identity_consistency"] = (
                1 - df[identity_cols]
                .isna()
                .mean(axis=1)
            )
        else:
            df["identity_consistency"] = 0

        # Device consistency
        df["device_consistency"] = np.where(
            df["DeviceType"].isna(),
            0,
            1
        )

        # Address consistency
        df["address_consistency"] = np.where(
            df["addr1"].notna()
            & df["addr2"].notna(),
            1,
            0
        )

        # Previous transaction count
        df["previous_transaction_count"] = (
            df.groupby("card1")
            .cumcount()
        )

        # Card age
        df["card_age_months"] = (
            np.log1p(
                df["previous_transaction_count"]
            ) * 12
        )

        # Overall data quality
        df["missingness_quality"] = (
            1 -
            df.isna()
            .mean(axis=1)
        )

        return df