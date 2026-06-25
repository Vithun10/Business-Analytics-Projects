class CreditEngine:

    def risk(
        self,
        credit_score
    ):

        credit_risk = (
            1
            -
            (
                credit_score
                / 100
            )
        )

        return credit_risk