from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.repositories.transaction_repository import (
    TransactionRepository
)

from app.services.ai_analyst_service import (
    AIRiskAnalystService
)

from app.services.decision_justification_service import (
    DecisionJustificationService
)

router = APIRouter()


@router.get(
    "/ai-analyst/{transaction_id}"
)
def ai_analysis(
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

    return (
        AIRiskAnalystService()
        .analyze(
            transaction,
            reasons
        )
    )