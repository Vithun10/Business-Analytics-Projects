from pydantic import BaseModel


class TransactionResponse(
    BaseModel
):

    transaction_id: str

    customer_id: str

    transaction_amount: float

    fraud_score: float

    credit_score: float

    credit_risk: float

    unified_risk_score: float

    risk_tier: str

    decision: str

    review_status: str

    class Config:

        from_attributes = True