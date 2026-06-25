from app.repositories.audit_repository import (
    AuditRepository
)


class AuditService:

    def __init__(self):

        self.repository = (
            AuditRepository()
        )

    def log(
        self,
        db,
        transaction_id,
        action,
        performed_by
    ):

        return (
            self.repository.create(
                db,
                transaction_id,
                action,
                performed_by
            )
        )