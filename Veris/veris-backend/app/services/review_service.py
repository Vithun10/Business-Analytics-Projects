from app.repositories.transaction_repository import (
    TransactionRepository
)

from app.services.audit_service import (
    AuditService
)


class ReviewService:

    def __init__(self):

        self.transaction_repository = (
            TransactionRepository()
        )

        self.audit_service = (
            AuditService()
        )

    def review_transaction(
        self,
        db,
        transaction_id,
        reviewer
    ):

        transaction = (
            self.transaction_repository
            .get_by_transaction_id(
                db,
                transaction_id
            )
        )

        if not transaction:

            return None

        transaction.review_status = (
            "REVIEWED"
        )

        db.commit()

        self.audit_service.log(
            db=db,
            transaction_id=transaction_id,
            action="TRANSACTION_REVIEWED",
            performed_by=reviewer
        )

        return transaction