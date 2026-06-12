"""fetch_data.py -- (re)create sample_data/sp500_returns.csv from Yahoo Finance.

The replication notebook reads the FROZEN sample_data/sp500_returns.csv that
ships with this repository, so you do NOT need to run this script to reproduce
the paper. It is provided only to document data provenance and to let you
refresh the panel.

Output schema (long/tidy, one row per ticker-day):
    date, ticker, log_ret_pct
where log_ret_pct = 100 * ( ln(P_t) - ln(P_{t-1}) ) on the adjusted close.

Usage:
    pip install yfinance pandas numpy
    python fetch_data.py            # writes sp500_returns.csv next to this file
"""
import os
import numpy as np
import pandas as pd

TICKERS = {
    "SP500": "^GSPC",   # S&P 500 index
    "XLE":   "XLE",     # Energy Select Sector SPDR
    "XLF":   "XLF",     # Financial Select Sector SPDR
    "XLK":   "XLK",     # Technology Select Sector SPDR
    "XLV":   "XLV",     # Health Care Select Sector SPDR
}
START = "1990-01-01"
END   = "2026-05-30"
OUT   = os.path.join(os.path.dirname(__file__), "sp500_returns.csv")


def main():
    import yfinance as yf  # imported lazily so the repo runs without yfinance
    frames = []
    for label, symbol in TICKERS.items():
        df = yf.download(symbol, start=START, end=END, auto_adjust=True,
                         progress=False)
        if df.empty:
            print(f"  WARNING: no data for {label} ({symbol})")
            continue
        px = df["Close"].dropna()
        logret = 100.0 * np.log(px).diff().dropna()
        frames.append(pd.DataFrame({
            "date": logret.index.strftime("%Y-%m-%d"),
            "ticker": label,
            "log_ret_pct": logret.values.ravel(),
        }))
        print(f"  {label:<6} {len(logret):>6} obs  "
              f"{logret.index.min().date()} -> {logret.index.max().date()}")
    panel = pd.concat(frames, ignore_index=True)
    panel.to_csv(OUT, index=False)
    print(f"\nWrote {len(panel):,} rows to {OUT}")


if __name__ == "__main__":
    main()
