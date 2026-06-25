import pandas as pd

from app.ml.fraud_engine import FraudEngine


df = pd.read_csv(
    "processed/feature_engineered.csv"
)

engine = FraudEngine()

scores = engine.score(
    df.head(10)
)

print("\nFraud Scores:")
print(scores)

print("\nMinimum Score:")
print(scores.min())

print("\nMaximum Score:")
print(scores.max())

print("\nAverage Score:")
print(scores.mean())