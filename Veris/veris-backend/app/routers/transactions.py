from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.repositories.transaction_repository import (
    TransactionRepository
)

from app.services.review_service import (
    ReviewService
)

review_service = (
    ReviewService()
)

router = APIRouter()

repository = (
    TransactionRepository()
)


@router.get(
    "/transactions"
)
def get_transactions(
    page: int = 1,
    page_size: int = 20,
    decision: str = None,
    risk_tier: str = None,
    transaction_id: str = None,
    db: Session = Depends(get_db)
):

    transactions = (
        repository.get_transactions(
            db=db,
            page=page,
            page_size=page_size,
            decision=decision,
            risk_tier=risk_tier,
            transaction_id=transaction_id
        )
    )

    return transactions

@router.patch(
    "/decisions/{transaction_id}/review"
)
def review_transaction(
    transaction_id: str,
    reviewer: str,
    db: Session = Depends(get_db)
):

    transaction = (
        review_service.review_transaction(
            db=db,
            transaction_id=transaction_id,
            reviewer=reviewer
        )
    )

    if not transaction:

        return {
            "message":
            "Transaction not found"
        }

    return {
        "message":
        "Transaction reviewed",
        "transaction_id":
        transaction_id
    }

@router.get(
    "/transactions/{transaction_id}"
)
def get_transaction_by_id(
    transaction_id: str,
    db: Session = Depends(get_db)
):

    transaction = (

        db.query(Transaction)

        .filter(
            Transaction.transaction_id
            == transaction_id
        )

        .first()
    )

    if not transaction:

        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return transaction