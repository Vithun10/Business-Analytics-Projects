from sqlalchemy.orm import Session

from app.models.db_models import Transaction


class TransactionRepository:

    def create(
        self,
        db,
        transaction_data
    ):

        transaction = Transaction(
            **transaction_data
        )

        db.add(transaction)
        db.commit()
        db.refresh(transaction)

        return transaction

    def get_transactions(
        self,
        db: Session,
        page: int = 1,
        page_size: int = 20,
        decision: str = None,
        risk_tier: str = None,
        transaction_id: str = None
    ):

        query = db.query(Transaction)

        if decision:
            query = query.filter(
                Transaction.decision == decision
            )

        if risk_tier:
            query = query.filter(
                Transaction.risk_tier == risk_tier
            )

        if transaction_id:
            query = query.filter(
                Transaction.transaction_id == transaction_id
            )

        return (
            query
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

    def get_by_transaction_id(
        self,
        db: Session,
        transaction_id: str
    ):

        return (
            db.query(Transaction)
            .filter(
                Transaction.transaction_id
                == transaction_id
            )
            .first()
        )
    
    def bulk_create(
        self,
        db: Session,
        transactions
    ):

        db.bulk_insert_mappings(
            Transaction,
            transactions
        )

        db.commit()

def get_by_transaction_id(
    self,
    db,
    transaction_id
):

    return (
        db.query(Transaction)
        .filter(
            Transaction.transaction_id
            ==
            transaction_id
        )
        .first()
    )