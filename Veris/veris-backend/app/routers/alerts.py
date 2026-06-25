from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.db_models import Transaction

router = APIRouter()


@router.get("/alerts")
def get_alerts(
    db: Session = Depends(get_db)
):

    alerts = []

    transactions = (
        db.query(Transaction)
        .all()
    )

    total = len(transactions)

    if total == 0:

        return []

    decline_count = len(
        [
            t
            for t in transactions
            if t.decision == "DECLINE"
        ]
    )

    review_count = len(
        [
            t
            for t in transactions
            if t.decision == "REVIEW"
        ]
    )

    approve_count = len(
        [
            t
            for t in transactions
            if t.decision == "APPROVE"
        ]
    )

    avg_urs = (

        sum(
            t.unified_risk_score
            for t in transactions
        )

        /

        total
    )

    if decline_count > 10:

        alerts.append({

            "severity":
                "HIGH",

            "message":
                f"{decline_count} declined transactions detected"
        })

    if review_count > approve_count:

        alerts.append({

            "severity":
                "MEDIUM",

            "message":
                "Review queue exceeds approvals"
        })

    if avg_urs > 0.60:

        alerts.append({

            "severity":
                "HIGH",

            "message":
                "Average portfolio risk exceeds threshold"
        })

    if not alerts:

        alerts.append({

            "severity":
                "INFO",

            "message":
                "No active risk alerts"
        })

    return alerts