from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.db_models import Transaction

from app.ml.shap_engine import (
    ShapEngine
)

router = APIRouter()


@router.get(
    "/shap/{transaction_id}"
)
def shap_explanation(
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

    return (

        ShapEngine()
        .explain(transaction)
    )