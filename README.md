# Threshold-Dependent Dominance in Tail Risk Approximation — Replication

Replication package for:

> Agbeyegbe, T. D. (2026). *Threshold-Dependent Dominance in Tail Risk
> Approximation.* **Econometrics** (MDPI), forthcoming.
> https://doi.org/10.3390/econometrics1010000

The paper compares the fourth-order **Edgeworth** expansion and the four-cumulant
**saddlepoint** approximation for tail-risk measurement in rare-disaster and
heavy-tailed financial settings. It derives a closed-form admissibility envelope
for the fourth-order Edgeworth density in the (γ₁, γ₂) plane, shows that **87.5%**
of 648 calibrated rare-disaster moment configurations fall outside it, and documents
that Edgeworth's mean Expected-Shortfall error rises from **6.20%** inside the
envelope to **47.04%** outside it, while the saddlepoint error stays near **13.64%**.

Running the notebook end-to-end reproduces **every table (Tables 1–11), both
manuscript figures, the three Supplementary Figures (S1–S3), and every headline
statistic** in the published version from a single deterministic pass. Notebook
table numbering matches the manuscript one-to-one.

## Contents

| Path | Purpose |
|---|---|
| `EdgeworthSaddlepoint_replication.ipynb` | Main notebook. Builds the 648-cell rare-disaster grid; derives the Edgeworth validity envelope in closed form (Proposition 1); computes Edgeworth and saddlepoint tail probabilities and Expected Shortfall; runs the Student-t / Hansen skewed-t / GED / two-sided-jump / generalised-hyperbolic robustness sweeps; classifies rolling empirical moments against the envelope; computes the per-ticker kurtosis-exceedance and plug-in exceedance-error tables; assembles the criterion-dominance summary; runs the Monte Carlo validation; and emits all tables and figures. |
| `sample_data/sp500_returns.csv` | Frozen daily log-return panel (percent) for the S&P 500 and the XLE / XLF / XLK / XLV sector ETFs, 1990–2026 (retrieved 8 May 2026). Used by the empirical-anchoring section. See `sample_data/README.md`. |
| `sample_data/fetch_data.py` | Provenance: (re)creates the panel from Yahoo Finance via `yfinance` (executed with yfinance 0.2.66). Not needed for replication — the frozen CSV ships with the repo. |
| `outputs/` | Reference outputs produced by the notebook: `table1`–`table11` CSVs matching the manuscript tables one-to-one, one auxiliary diagnostic CSV (`auxiliary_empirical_regime.csv`, not a manuscript table), the robustness CSVs, the closed-form envelope, and the two manuscript figures. Provided so reviewers can diff against a fresh run. |
| `supplementary/` | Supplementary Figures S1–S3 as published with the article (cited in Sections 4.5 and 4.7 of the paper) and their description. |

## How to run

### Locally

```bash
git clone https://github.com/ProfTemi/threshold-risk-replication.git
cd threshold-risk-replication
pip install -r requirements.txt
jupyter notebook EdgeworthSaddlepoint_replication.ipynb   # Kernel → Restart & Run All
```

A full run takes ≈ 4–5 minutes on a laptop CPU. All outputs are written to `outputs/`,
and the two manuscript figures (`figure1_preview.pdf`, `figure2_preview.pdf`) are also
written to the working directory so they can be picked up directly by the LaTeX source.

### Google Colab

Open the notebook in Colab, upload `sample_data/sp500_returns.csv` to a `sample_data/`
folder, then *Runtime → Run all*.

## Reproducibility

- The committed notebook was executed under **Python 3.12.13**; any Python ≥ 3.10
  with the pinned requirements reproduces the same numbers.
- The notebook sets `np.random.seed(456)`, so the Monte Carlo cells are deterministic
  (true tail probability `0.011109`, MC mean `0.011067`, Edgeworth error `194.44%`,
  saddlepoint error `88.08%`; manuscript Table 9).
- The empirical section reads the **frozen** `sample_data/sp500_returns.csv` rather than
  calling `yfinance` live, so the rolling-moment and per-ticker tables (manuscript
  Tables 7 and 8) are bit-reproducible and do not drift with Yahoo Finance's
  retroactive adjustments.
- The lateral peak of the Edgeworth envelope is found by continuous optimization
  (`scipy.optimize.minimize_scalar`), reproducing `|γ₁*| ≈ 0.6846` at `γ₂ ≈ 2.533`
  independent of plotting resolution.

### Note on the four-cumulant saddlepoint

The truncated four-cumulant cumulant-generating function is non-convex when
`κ₄ < 0` (sub-Gaussian / thin-tailed distributions), so the saddlepoint is
mathematically undefined there. The implementation flags such cells and records them
as missing (`NaN`) rather than substituting a value; they are excluded from the
saddlepoint error averages. This affects only the two sub-Gaussian GED cells
(ν = 3, 5) in Table 6; every other family and the entire rare-disaster grid are
well-posed.

## Requirements

Python ≥ 3.10 with `numpy`, `scipy`, `pandas`, `matplotlib` (see `requirements.txt`).

## Acknowledgments

The author thanks Toneukarin G. Agbeyegbe for research assistance and helpful
discussions throughout the development of this package.
