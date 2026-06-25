import os
from pathlib import Path

import joblib
from huggingface_hub import hf_hub_download

from dotenv import load_dotenv

load_dotenv()

MODEL_REPO = os.getenv("HF_MODEL_REPO")
MODEL_FILENAME = os.getenv(
    "HF_MODEL_FILENAME",
    "veris_fraud_rf.pkl"
)
HF_TOKEN = os.getenv("HF_TOKEN")


def load_rf_model():
    """
    Load Random Forest model.

    Priority:
    1. Local model (development)
    2. Hugging Face (production)
    """

    local_model = Path("app/ml/artifacts") / MODEL_FILENAME

    if local_model.exists():
        print(f"✓ Loading local RF model: {local_model}")
        return joblib.load(local_model)

    print("Local RF model not found.")
    print("Downloading RF model from Hugging Face...")

    downloaded_model = hf_hub_download(
        repo_id=MODEL_REPO,
        filename=MODEL_FILENAME,
        token=HF_TOKEN,
    )

    print(f"✓ RF model downloaded: {downloaded_model}")

    return joblib.load(downloaded_model)