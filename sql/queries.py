import pandas as pd
import sqlite3

# Load analyzed data into a SQLite database (stored in memory)
df = pd.read_csv("data/sp500_analyzed.csv")
conn = sqlite3.connect(":memory:")
df.to_sql("sp500", conn, index=False, if_exists="replace")

# --- Query 1: Average health score by sector ---
q1 = """
SELECT sector,
       ROUND(AVG(health_score), 2) AS avg_health_score,
       COUNT(*) AS num_companies
FROM sp500
GROUP BY sector
ORDER BY avg_health_score DESC
"""
print("=== Average Health Score by Sector ===")
print(pd.read_sql(q1, conn))

# --- Query 2: Top 5 companies per sector by health score ---
q2 = """
SELECT sector, ticker, company,
       ROUND(health_score, 2) AS health_score
FROM sp500
WHERE health_score >= 40
ORDER BY sector, health_score DESC
"""
print("\n=== Companies with Health Score >= 40 ===")
print(pd.read_sql(q2, conn))

# --- Query 3: Highest operating margin per sector ---
q3 = """
SELECT sector, ticker, company,
       ROUND(op_margin_pct, 2) AS operating_margin
FROM sp500
ORDER BY op_margin_pct DESC
LIMIT 10
"""
print("\n=== Top 10 Companies by Operating Margin ===")
print(pd.read_sql(q3, conn))

conn.close()
