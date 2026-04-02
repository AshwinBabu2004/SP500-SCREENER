import pandas as pd

# Load the clean data
df = pd.read_csv("data/sp500_clean.csv")

# --- Calculate Metrics ---

# ROE is already provided by Yahoo Finance (as a decimal, e.g. 0.25 = 25%)
df["roe_pct"] = df["return_on_equity"] * 100

# Debt-to-Equity already provided — just rename for clarity
df["d_to_e"] = df["debt_to_equity"]
df["roe_pct"] = df["return_on_equity"] * 100

# Cap ROE at 200% to prevent outliers from skewing the score
df["roe_pct"] = df["roe_pct"].clip(upper=200)


# Operating Margin already provided (as decimal, convert to %)
df["op_margin_pct"] = df["operating_margin"] * 100

# EPS Growth: how much EPS is expected to grow (forward vs trailing)
df["eps_growth_pct"] = ((df["eps_forward"] - df["eps"]) / df["eps"].abs()) * 100

# --- Build Composite Health Score (0 to 100) ---

def score_column(series):
    """Scale any column to a 0–100 score based on min/max"""
    return (series - series.min()) / (series.max() - series.min()) * 100

df["score_roe"]        = score_column(df["roe_pct"])
df["score_de"]         = score_column(-df["d_to_e"])   # negative: lower debt = better
df["score_margin"]     = score_column(df["op_margin_pct"])
df["score_eps_growth"] = score_column(df["eps_growth_pct"])

# Average the 4 scores into one composite score
df["health_score"] = (
    df["score_roe"] +
    df["score_de"] +
    df["score_margin"] +
    df["score_eps_growth"]
) / 4

# --- Preview Results ---
cols = ["ticker", "company", "sector", "roe_pct", "d_to_e", "op_margin_pct", "eps_growth_pct", "health_score"]
print(df[cols].sort_values("health_score", ascending=False).head(10))

# Save
df.to_csv("data/sp500_analyzed.csv", index=False)
print("\nSaved to data/sp500_analyzed.csv")
