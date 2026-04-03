# S&P 500 Financial Health Screener

Analyzes 50 S&P 500 companies across 8 sectors using Python and SQL.

## What it does
- Downloads live financial data from Yahoo Finance
- Calculates key metrics: ROE, Debt-to-Equity, Operating Margin, EPS Growth
- Builds a composite financial health score (0–100) per company
- Uses SQL to compare performance across sectors
- Exports results to Excel for Tableau dashboards

## Tech Stack
Python, Pandas, SQLite, yfinance, tableau

## Files
- `notebooks/download_data.py` — data collection
- `notebooks/clean_data.py` — data cleaning
- `notebooks/analyze.py` — metric calculation and scoring
- `sql/queries.py` — sector-level SQL analysis
- `notebooks/export.py` — Tableau export

## Dashboard
[View Tableau Dashboard](https://public.tableau.com/views/SP500FInancialHealthScreener/SP500FinancialHealthScreener)
