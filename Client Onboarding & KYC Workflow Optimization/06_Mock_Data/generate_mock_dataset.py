"""
Mock dataset generator v2 - Client Onboarding & KYC Workflow Optimization
Fixes v1's bug: risk_score distribution topped out at ~69, so thresholds
70/75 were above the entire population and produced no real comparison.

DESIGN NOTE (not a real-world claim): the deceptive-profile injection rate
below is a synthetic-data design choice made purely to ensure the dataset
has a populated, analyzable borderline zone around the threshold. It does
NOT represent any real-world fraud/risk prevalence statistic and must not
be cited as such in the case study.
"""

import pandas as pd
import numpy as np

SEED = 42
rng = np.random.default_rng(SEED)
N_ROWS = 2000

# --- Country risk reference (toy list, not a real regulatory list) ---
# FIX: widened spread and gave higher-risk countries more sampling weight
# so country_risk_score actually contributes meaningful range.
countries = {
    "Switzerland": 8, "Germany": 12, "Singapore": 10, "UK": 15,
    "USA": 18, "India": 38, "UAE": 42, "Brazil": 48,
    "Nigeria": 70, "Russia": 78, "Cayman Islands": 82, "Iran": 96,
}
country_names = list(countries.keys())
country_base_risk = np.array(list(countries.values()))

# FIX: less skew toward only-safe countries (was 15/10/20/15/8/10/8/4/3/2/1/4)
country_weights = np.array([12, 10, 8, 10, 12, 14, 10, 8, 6, 5, 3, 2], dtype=float)
country_weights /= country_weights.sum()
applicant_country = rng.choice(country_names, size=N_ROWS, p=country_weights)
country_risk_base = np.array([countries[c] for c in applicant_country])
country_risk_score = np.clip(country_risk_base + rng.normal(0, 9, N_ROWS), 0, 100)

# --- Transaction velocity score ---
# FIX: gamma(2, 12) had mean ~24 and a thin tail. Switched to gamma(2.2, 18)
# for mean ~40 with a fatter right tail, so high-velocity cases are real.
transaction_velocity_score = np.clip(rng.gamma(shape=2.2, scale=18, size=N_ROWS), 0, 100)

# --- Verification match rate ---
# FIX: beta(6,1.3) skewed too high (mean ~82), crushing (100-match_rate).
# beta(5,1.8) -> mean ~73, more realistic failure tail.
verification_match_rate = np.clip(rng.beta(a=5, b=1.8, size=N_ROWS) * 100, 0, 100)

# --- Deceptive profiles (~12%) ---
# FIX: stronger injection (was +25..+55, now +40..+70) so the bump actually
# pushes scores into the 65-90 band instead of being absorbed by low weights.
n_deceptive = int(N_ROWS * 0.12)
deceptive_idx = rng.choice(N_ROWS, size=n_deceptive, replace=False)
deceptive_type = rng.integers(0, 3, size=n_deceptive)
for i, idx in enumerate(deceptive_idx):
    t = deceptive_type[i]
    if t == 0:
        country_risk_score[idx] = np.clip(country_risk_score[idx] + rng.uniform(40, 70), 0, 100)
    elif t == 1:
        transaction_velocity_score[idx] = np.clip(transaction_velocity_score[idx] + rng.uniform(40, 70), 0, 100)
    else:
        verification_match_rate[idx] = np.clip(verification_match_rate[idx] - rng.uniform(40, 65), 0, 100)

# --- risk_score per FRD FR-002/FR-003 (placeholder weights 40/30/30) ---
W_COUNTRY, W_VELOCITY, W_VERIFICATION = 0.40, 0.30, 0.30
risk_score = np.clip(
    country_risk_score * W_COUNTRY
    + transaction_velocity_score * W_VELOCITY
    + (100 - verification_match_rate) * W_VERIFICATION,
    0, 100
)

# --- PEP flag (~4%, independent of risk_score) ---
is_pep = rng.choice([True, False], size=N_ROWS, p=[0.04, 0.96])

# --- risk_tier per FR-004 (placeholder thresholds) + FR-005 PEP override ---
risk_tier = np.where(risk_score < 50, "Low", np.where(risk_score < 75, "Medium", "High"))
risk_tier = np.where(is_pep, "High", risk_tier)

# --- Ground-truth outcome: correlated with risk_score but genuinely noisy ---
# FIX: v1's true_risk_signal weights (.35/.25/.20) were too similar to
# risk_score's own weights (.40/.30/.30) AND used the same three inputs with
# only one noise draw -- nearly perfectly correlated, leaving no room for
# real false positives/negatives. Now: bigger independent noise (sigma 25,
# was 18) and a lower, more central cutoff so the boundary actually sits
# inside the populated range rather than out past it.
true_risk_signal = np.clip(
    country_risk_score * 0.35
    + transaction_velocity_score * 0.25
    + (100 - verification_match_rate) * 0.20
    + rng.normal(0, 25, N_ROWS),
    0, 100
)
outcome = np.where(true_risk_signal >= 55, "flagged_risky", "legitimate")
pep_extra_risk = rng.random(N_ROWS) < 0.55
outcome = np.where(is_pep & pep_extra_risk, "flagged_risky", outcome)

# --- Funnel stage reached ---
funnel_stages = ["signup_started", "details_entered", "document_uploaded",
                  "selfie_uploaded", "verification_complete", "activated"]
drop_prob_base = np.select(
    [risk_tier == "Low", risk_tier == "Medium", risk_tier == "High"],
    [0.12, 0.22, 0.30]
)
drop_prob = np.clip(drop_prob_base + (100 - verification_match_rate) / 400, 0, 0.85)
funnel_stage_reached = []
for p in drop_prob:
    if rng.random() < p:
        stage = rng.choice(funnel_stages[:5], p=[0.10, 0.15, 0.40, 0.25, 0.10])
    else:
        stage = "activated"
    funnel_stage_reached.append(stage)
funnel_stage_reached = np.array(funnel_stage_reached)

# --- TTO in minutes ---
tto_base = np.select([risk_tier == "Low", risk_tier == "Medium", risk_tier == "High"], [4, 18, 55])
tto_minutes = np.clip(tto_base + rng.normal(0, tto_base * 0.3, N_ROWS), 1, None)
tto_minutes = np.where(funnel_stage_reached == "activated", tto_minutes, np.nan)

# --- Timestamps ---
start_dates = pd.Timestamp("2025-01-01") + pd.to_timedelta(rng.integers(0, 180, N_ROWS), unit="D")

df = pd.DataFrame({
    "user_id": [f"U{str(i).zfill(5)}" for i in range(N_ROWS)],
    "country": applicant_country,
    "transaction_velocity_score": np.round(transaction_velocity_score, 2),
    "verification_match_rate": np.round(verification_match_rate, 2),
    "country_risk_score": np.round(country_risk_score, 2),
    "is_pep": is_pep,
    "risk_score": np.round(risk_score, 2),
    "risk_tier": risk_tier,
    "outcome": outcome,
    "timestamp": start_dates,
    "funnel_stage_reached": funnel_stage_reached,
    "tto_minutes": np.round(tto_minutes, 1),
})

df.to_csv("mock_onboarding_dataset.csv", index=False)
print(f"Generated {len(df)} rows -> mock_onboarding_dataset.csv")
print(df["risk_score"].describe())