import numpy as np
import pandas as pd


class ProxyCreditEngine:

    def score(
        self,
        df: pd.DataFrame
    ):

        working_df = df

        # ----------------------------------
        # Card Age Score
        # ----------------------------------

        card_age_score = np.minimum(
            (
                working_df["card_age_months"]
                + 12
            )
            / 60,
            1
        )

        # ----------------------------------
        # Device Consistency
        # ----------------------------------

        device_score = (
            working_df["device_consistency"]
        )

        # ----------------------------------
        # Identity Consistency
        # ----------------------------------

        identity_score = (
            working_df["identity_consistency"]
        )

        # ----------------------------------
        # Address Consistency
        # ----------------------------------

        address_score = (
            working_df["address_consistency"]
        )

        # ----------------------------------
        # Historical Activity
        # ----------------------------------

        historical_score = np.minimum(
            (
                working_df[
                    "previous_transaction_count"
                ]
                + 10
            )
            / 100,
            1
        )

        # ----------------------------------
        # Missingness Quality
        # ----------------------------------

        missingness_score = (
            working_df["missingness_quality"]
        )

        # ----------------------------------
        # Credit Score
        # ----------------------------------

        credit_score = (
            (
                0.25 * card_age_score
                +
                0.20 * device_score
                +
                0.20 * identity_score
                +
                0.15 * address_score
                +
                0.15 * historical_score
                +
                0.05 * missingness_score
            )
            * 100
        )

        credit_score = np.clip(
            credit_score,
            0,
            100
        )

        return credit_score