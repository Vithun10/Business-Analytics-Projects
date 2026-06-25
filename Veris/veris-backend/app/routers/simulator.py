from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class SimulationRequest(BaseModel):

    fraud_score: float
    credit_risk: float


@router.post("/simulator")
def simulate_risk(
    request: SimulationRequest
):

    urs = (

        (0.6 * request.fraud_score)

        +

        (0.4 * request.credit_risk)
    )

    if urs < 0.40:

        decision = "APPROVE"
        risk_tier = "LOW"

    elif urs <= 0.70:

        decision = "REVIEW"
        risk_tier = "MEDIUM"

    else:

        decision = "DECLINE"
        risk_tier = "HIGH"

    return {

        "fraud_score":
            request.fraud_score,

        "credit_risk":
            request.credit_risk,

        "urs":
            round(urs, 4),

        "decision":
            decision,

        "risk_tier":
            risk_tier
    }