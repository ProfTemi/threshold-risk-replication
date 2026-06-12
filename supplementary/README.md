# Supplementary figures

Auxiliary diagnostics produced by the replication notebook (Section 16). These
are **not** numbered figures in the manuscript — the two manuscript figures are
`figure1_preview.pdf` (density + tail-error panel) and `figure2_preview.pdf`
(admissibility geometry), found in `../outputs/`. The plots below provide
additional visual support for the robustness and empirical-anchoring sections.

| File | Description |
|---|---|
| `supplementary_figureS1_validity_envelope.{pdf,png}` | Edgeworth validity envelope over the 648-cell rare-disaster grid, plotted in (\|γ₁\|, γ₂) coordinates, with the closed-form kurtosis ceiling γ₂ = 4 and the lateral peak \|γ₁*\| ≈ 0.685. A coordinate-transposed companion to manuscript Figure 2. |
| `supplementary_figureS2_distributions_overlay.{pdf,png}` | The same envelope with the four alternative families (Hansen skewed-t, GED, two-sided jump, generalised hyperbolic) overlaid, showing where each family's moment configurations fall relative to the Edgeworth admissible region. |
| `supplementary_figureS3_empirical_trajectory.{pdf,png}` | S&P 500 rolling 250-day (γ₁, γ₂) trajectory with the 1998 LTCM, 2008 GFC, 2020 COVID, and 2022 inflation stress windows highlighted, illustrating how realized moments leave the validity envelope during recognized stress episodes. |

All three regenerate deterministically when the notebook is run end-to-end.
