from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models.db_models import Transaction

router = APIRouter()


@router.get("/analytics/summary")
def analytics_summary(
    db: Session = Depends(get_db)
):

    total_transactions = (
        db.query(Transaction)
        .count()
    )

    approve_count = (
        db.query(Transaction)
        .filter(
            Transaction.decision == "APPROVE"
        )
        .count()
    )

    review_count = (
        db.query(Transaction)
        .filter(
            Transaction.decision == "REVIEW"
        )
        .count()
    )

    decline_count = (
        db.query(Transaction)
        .filter(
            Transaction.decision == "DECLINE"
        )
        .count()
    )

    average_fraud_score = (
        db.query(
            func.avg(
                Transaction.fraud_score
            )
        )
        .scalar()
    )

    average_credit_score = (
        db.query(
            func.avg(
                Transaction.credit_score
            )
        )
        .scalar()
    )

    average_urs = (
        db.query(
            func.avg(
                Transaction.unified_risk_score
            )
        )
        .scalar()
    )

    return {

        "total_transactions":
            total_transactions,

        "approve_count":
            approve_count,

        "review_count":
            review_count,

        "decline_count":
            decline_count,

        "average_fraud_score":
            round(
                average_fraud_score or 0,
                4
            ),

        "average_credit_score":
            round(
                average_credit_score or 0,
                4
            ),

        "average_urs":
            round(
                average_urs or 0,
                4
            )
    }

@router.get(
    "/dashboard/overview"
)
def dashboard_overview(
    db: Session = Depends(get_db)
):

    total_transactions = (
        db.query(Transaction)
        .count()
    )

    approve_count = (
        db.query(Transaction)
        .filter(
            Transaction.decision == "APPROVE"
        )
        .count()
    )

    review_count = (
        db.query(Transaction)
        .filter(
            Transaction.decision == "REVIEW"
        )
        .count()
    )

    decline_count = (
        db.query(Transaction)
        .filter(
            Transaction.decision == "DECLINE"
        )
        .count()
    )

    average_fraud_score = (
        db.query(
            func.avg(
                Transaction.fraud_score
            )
        )
        .scalar()
    )

    average_credit_score = (
        db.query(
            func.avg(
                Transaction.credit_score
            )
        )
        .scalar()
    )

    average_urs = (
        db.query(
            func.avg(
                Transaction.unified_risk_score
            )
        )
        .scalar()
    )

    return {

        "total_transactions":
            total_transactions,

        "approve_count":
            approve_count,

        "review_count":
            review_count,

        "decline_count":
            decline_count,

        "average_fraud_score":
            round(
                average_fraud_score or 0,
                4
            ),

        "average_credit_score":
            round(
                average_credit_score or 0,
                4
            ),

        "average_urs":
            round(
                average_urs or 0,
                4
            )
    }

@router.get(
    "/dashboard/risk-distribution"
)
def risk_distribution(
    db: Session = Depends(get_db)
):

    low = (
        db.query(Transaction)
        .filter(
            Transaction.risk_tier == "LOW"
        )
        .count()
    )

    medium = (
        db.query(Transaction)
        .filter(
            Transaction.risk_tier == "MEDIUM"
        )
        .count()
    )

    high = (
        db.query(Transaction)
        .filter(
            Transaction.risk_tier == "HIGH"
        )
        .count()
    )

    return {

        "LOW": low,

        "MEDIUM": medium,

        "HIGH": high
    }

@router.get(
    "/dashboard/decision-distribution"
)
def decision_distribution(
    db: Session = Depends(get_db)
):

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

        "APPROVE": approve,

        "REVIEW": review,

        "DECLINE": decline
    }

@router.get(
    "/dashboard/fraud-metrics"
)
def fraud_metrics(
    db: Session = Depends(get_db)
):

    avg_fraud_score = (
        db.query(
            func.avg(
                Transaction.fraud_score
            )
        )
        .scalar()
    )

    max_fraud_score = (
        db.query(
            func.max(
                Transaction.fraud_score
            )
        )
        .scalar()
    )

    min_fraud_score = (
        db.query(
            func.min(
                Transaction.fraud_score
            )
        )
        .scalar()
    )

    return {

        "average":
            round(
                avg_fraud_score or 0,
                4
            ),

        "maximum":
            round(
                max_fraud_score or 0,
                4
            ),

        "minimum":
            round(
                min_fraud_score or 0,
                4
            )
    }

@router.get(
    "/dashboard/credit-metrics"
)
def credit_metrics(
    db: Session = Depends(get_db)
):

    avg_credit = (
        db.query(
            func.avg(
                Transaction.credit_score
            )
        )
        .scalar()
    )

    max_credit = (
        db.query(
            func.max(
                Transaction.credit_score
            )
        )
        .scalar()
    )

    min_credit = (
        db.query(
            func.min(
                Transaction.credit_score
            )
        )
        .scalar()
    )

    return {

        "average":
            round(
                avg_credit or 0,
                4
            ),

        "maximum":
            round(
                max_credit or 0,
                4
            ),

        "minimum":
            round(
                min_credit or 0,
                4
            )
    }