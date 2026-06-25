import pandas as pd

from app.ml.feature_pipeline import FeaturePipeline

df = pd.read_csv(
    "processed/merged_transactions.csv"
)

print("Loaded:", df.shape)

for col in df.select_dtypes(include=["float64"]).columns:
    df[col] = df[col].astype("float32")

for col in df.select_dtypes(include=["int64"]).columns:
    df[col] = df[col].astype("int32")

pipeline = FeaturePipeline()

result = pipeline.transform(df)

result.to_csv(
    "processed/feature_engineered.csv",
    index=False
)

print(f"Saved {len(result)} records")