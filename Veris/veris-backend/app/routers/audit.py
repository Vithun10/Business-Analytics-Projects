from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.repositories.audit_repository import (
    AuditRepository
)

router = APIRouter()

repository = AuditRepository()


@router.get(
    "/audit-log"
)
def get_audit_log(
    db: Session = Depends(get_db)
):

    return (
        repository.get_all(
            db
        )
    )