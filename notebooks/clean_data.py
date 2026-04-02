import pandas as pd

# Load the raw data
df = pd.read_csv("data/sp500_raw.csv")

print("Shape before cleaning:", df.shape)

# Fill missing numeric values with the median of their column
# Median is better than average because it ignores extreme outliers
df["debt_to_equity"] = df["debt_to_equity"].fillna(df["debt_to_equity"].median())
df["return_on_equity"] = df["return_on_equity"].fillna(df["return_on_equity"].median())

# Remove any rows where critical fields are still missing
df = df.dropna(subset=["revenue", "net_income", "eps", "sector"])

# Reset the row numbers after dropping
df = df.reset_index(drop=True)

print("Shape after cleaning:", df.shape)
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Save the cleaned file
df.to_csv("data/sp500_clean.csv", index=False)
print("\nDone! Saved to data/sp500_clean.csv")




