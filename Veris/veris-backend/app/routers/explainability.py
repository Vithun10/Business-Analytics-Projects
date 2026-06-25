from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.repositories.transaction_repository import (
    TransactionRepository
)

from app.services.decision_justification_service import (
    DecisionJustificationService
)

router = APIRouter()


@router.get(
    "/explanations/{transaction_id}"
)
def get_explanation(
    transaction_id: str,
    db: Session = Depends(get_db)
):

    transaction = (
        TransactionRepository()
        .get_by_transaction_id(
            db,
            transaction_id
        )
    )

    if not transaction:

        return {
            "message":
            "Transaction not found"
        }

    reasons = (
        DecisionJustificationService()
        .generate(
            transaction
        )
    )

    return {

        "transaction_id":
            transaction.transaction_id,

        "decision":
            transaction.decision,

        "risk_tier":
            transaction.risk_tier,

        "fraud_score":
            transaction.fraud_score,

        "credit_score":
            transaction.credit_score,

        "credit_risk":
            transaction.credit_risk,

        "urs":
            transaction.unified_risk_score,

        "reasons":
            reasons
    }