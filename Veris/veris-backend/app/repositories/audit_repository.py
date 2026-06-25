from sqlalchemy.orm import Session

from app.models.db_models import AuditLog


class AuditRepository:

    def create(
        self,
        db: Session,
        transaction_id: str,
        action: str,
        performed_by: str
    ):

        audit = AuditLog(
            transaction_id=transaction_id,
            action=action,
            performed_by=performed_by
        )

        db.add(audit)

        db.commit()

        db.refresh(audit)

        return audit

    def get_all(
        self,
        db: Session
    ):

        return (
            db.query(AuditLog)
            .order_by(
                AuditLog.timestamp.desc()
            )
            .all()
        )