from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.db_models import Transaction

router = APIRouter()


@router.get(
    "/trends"
)
def trends(
    db: Session = Depends(get_db)
):

    total = (
        db.query(Transaction)
        .count()
    )

    approve = (
        db.query(Transaction)
        .filter(
            Transaction.decision == "APPROVE"
        )
        .count()
    )

    review = (
        db.query(Transaction)
        .filter(
            Transaction.decision == "REVIEW"
        )
        .count()
    )

    decline = (
        db.query(Transaction)
        .filter(
            Transaction.decision == "DECLINE"
        )
        .count()
    )

    return {

        "transaction_volume":
            total,

        "decision_trends": {

            "approve":
                approve,

            "review":
                review,

            "decline":
                decline
        }
    }