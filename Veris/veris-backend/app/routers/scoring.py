from fastapi import APIRouter

router = APIRouter()


@router.post(
    "/transactions/score"
)
def score_transactions():

    return {
        "message":
        "Scoring pipeline endpoint ready"
    }