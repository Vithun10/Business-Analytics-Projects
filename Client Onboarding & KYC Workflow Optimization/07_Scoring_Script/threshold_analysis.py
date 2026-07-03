"""
Threshold-tuning analysis — tests candidate thresholds (70 vs 75) against
the mock dataset's risk_score and ground-truth outcome columns.
"""

import pandas as pd

df = pd.read_csv("../06_Mock_Data/mock_onboarding_dataset.csv")

print("=" * 60)
print("1. RISK SCORE DISTRIBUTION SUMMARY")
print("=" * 60)
print(df["risk_score"].describe())

print("\n" + "=" * 60)
print("2. RISK SCORE BUCKET BREAKDOWN")
print("=" * 60)
buckets = pd.cut(df["risk_score"], bins=[0, 50, 60, 65, 70, 75, 80, 90, 100])
print(buckets.value_counts().sort_index())

print("\n" + "=" * 60)
print("3. THRESHOLD COMPARISON: FALSE POSITIVES / NEGATIVES")
print("=" * 60)
actual_risky = df["outcome"] == "flagged_risky"
for t in [70, 75]:
    predicted_high_risk = df["risk_score"] >= t
    fp = ((predicted_high_risk) & (~actual_risky)).sum()
    fn = ((~predicted_high_risk) & (actual_risky)).sum()
    tp = ((predicted_high_risk) & (actual_risky)).sum()
    tn = ((~predicted_high_risk) & (~actual_risky)).sum()
    precision = tp / (tp + fp) if (tp + fp) > 0 else float("nan")
    recall = tp / (tp + fn) if (tp + fn) > 0 else float("nan")
    print(f"\nThreshold = {t}")
    print(f"  True Positives:  {tp}")
    print(f"  False Positives: {fp}")
    print(f"  True Negatives:  {tn}")
    print(f"  False Negatives: {fn}")
    print(f"  Precision: {precision:.3f}  Recall: {recall:.3f}")

print("\n" + "=" * 60)
print("4. OVERALL OUTCOME SPLIT")
print("=" * 60)
print(df["outcome"].value_counts())
print(f"\nTotal rows: {len(df)}")

print("\n" + "=" * 60)
print("5. RISK TIER DISTRIBUTION (current placeholder thresholds)")
print("=" * 60)
print(df["risk_tier"].value_counts())