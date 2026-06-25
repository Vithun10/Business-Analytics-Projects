import pandas as pd

from sqlalchemy import text


class ExportService:

    def export_json(self, db):

        query = text("""
            SELECT *
            FROM transactions
        """)

        df = pd.read_sql(
            query,
            db.bind
        )

        return {
            "total_transactions": len(df),
            "transactions": df.to_dict(
                orient="records"
            )
        }

    def export_csv(self, db):

        query = text("""
            SELECT *
            FROM transactions
        """)

        df = pd.read_sql(
            query,
            db.bind
        )

        return df