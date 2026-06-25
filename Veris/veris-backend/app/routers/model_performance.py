from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/model-performance"
)
def model_performance():

    return {

        "random_forest": {

            "roc_auc": 0.8774,
            "precision": 0.2301,
            "recall": 0.6344,
            "f1_score": 0.3377
        },

        "xgboost": {

            "roc_auc": 0.8936,
            "precision": 0.1884,
            "recall": 0.7423,
            "f1_score": 0.3006
        }
    }