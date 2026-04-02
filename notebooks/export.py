import pandas as pd
import sqlite3

# Load analyzed data
df = pd.read_csv("data/sp500_analyzed.csv")

# --- Export 1: Company-level data ---
company_export = df[[
    "ticker", "company", "sector",
    "roe_pct", "d_to_e", "op_margin_pct",
    "eps_growth_pct", "health_score"
]].round(2)

company_export.to_excel("exports/company_scores.xlsx", index=False)
print("Saved: exports/company_scores.xlsx")

# --- Export 2: Sector summary via SQL ---
conn = sqlite3.connect(":memory:")
df.to_sql("sp500", conn, index=False, if_exists="replace")

sector_summary = pd.read_sql("""
    SELECT sector,
           COUNT(*) AS num_companies,
           ROUND(AVG(health_score), 2) AS avg_health_score,
           ROUND(AVG(roe_pct), 2) AS avg_roe,
           ROUND(AVG(d_to_e), 2) AS avg_debt_to_equity,
           ROUND(AVG(op_margin_pct), 2) AS avg_operating_margin
    FROM sp500
    GROUP BY sector
    ORDER BY avg_health_score DESC
""", conn)

sector_summary.to_excel("exports/sector_summary.xlsx", index=False)
print("Saved: exports/sector_summary.xlsx")

conn.close()
print("\nAll exports done! Open these files in Power BI.")
