# Market data — `sp500_returns.csv`

Frozen daily log-return panel used by the empirical-anchoring section
(Section 4.7–4.8, Tables 7–8, Supplementary Figure S3).

## Format

A long (tidy) CSV with one row per ticker-day:

| column | meaning |
|---|---|
| `date` | trading date (`YYYY-MM-DD`) |
| `ticker` | `SP500`, `XLE`, `XLF`, `XLK`, or `XLV` |
| `log_ret_pct` | daily log return in **percent**: `100 · (ln Pₜ − ln Pₜ₋₁)` on adjusted close |

## Coverage

| ticker | obs | start | end |
|---|---|---|---|
| SP500 | 9,168 | 1990-01-03 | 2026-05-29 |
| XLE | 6,899 | 1998-12-23 | 2026-05-29 |
| XLF | 6,899 | 1998-12-23 | 2026-05-29 |
| XLK | 6,899 | 1998-12-23 | 2026-05-29 |
| XLV | 6,899 | 1998-12-23 | 2026-05-29 |

The sector ETFs begin in December 1998 because the SPDR Select Sector funds
launched then; the S&P 500 series begins in 1990. After 250-day rolling windows
and `dropna`, these yield the window counts reported in Table 7 (8,904 for the
S&P 500 and 6,635 per ETF).

## Provenance

Daily adjusted closing prices were retrieved from Yahoo Finance via the
`yfinance` Python package and converted to percent log returns. The panel is
**frozen** here so the published Table 7 / Table 8 and Supplementary Figure S3
are bit-reproducible regardless of Yahoo Finance's subsequent retroactive
adjustments. `fetch_data.py` documents the retrieval step and can re-create the
panel from Yahoo Finance. No proprietary data are used.
