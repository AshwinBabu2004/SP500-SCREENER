import yfinance as yf
import pandas as pd
import os

# 50 S&P 500 companies across different sectors
tickers = [
    # Technology
    "AAPL", "MSFT", "NVDA", "GOOGL", "META", "ORCL", "IBM", "TXN", "QCOM", "ADBE",
    # Healthcare
    "JNJ", "UNH", "PFE", "ABBV", "MRK", "TMO", "ABT", "LLY", "MDT", "CVS",
    # Financials
    "JPM", "BAC", "WFC", "GS", "MS", "BLK", "AXP", "USB", "PNC", "C",
    # Consumer
    "AMZN", "WMT", "HD", "MCD", "NKE", "SBUX", "TGT", "COST", "PG", "KO",
    # Energy & Industrials
    "XOM", "CVX", "COP", "BA", "CAT", "GE", "HON", "UPS", "LMT", "RTX"
]

all_data = []

for ticker in tickers:
    print(f"Downloading: {ticker}")
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        all_data.append({
            "ticker": ticker,
            "company": info.get("longName"),
            "sector": info.get("sector"),
            "market_cap": info.get("marketCap"),
            "revenue": info.get("totalRevenue"),
            "net_income": info.get("netIncomeToCommon"),
            "total_debt": info.get("totalDebt"),
            "debt_to_equity": info.get("debtToEquity"),
            "operating_margin": info.get("operatingMargins"),
            "eps": info.get("trailingEps"),
            "eps_forward": info.get("forwardEps"),
            "return_on_equity": info.get("returnOnEquity"),
        })

    except Exception as e:
        print(f"  Skipped {ticker}: {e}")

df = pd.DataFrame(all_data)
df.to_csv("data/sp500_raw.csv", index=False)
print("\nDone! File saved to data/sp500_raw.csv")
print(df.shape)

