# Reproduction map

All commands run from a fresh common extraction root, in the order below.
The wrapper performs this sequence, logs exit codes, and stops on failure.
Original archive outputs are retained in the ZIP files; reanalysis writes to
the extraction directory only. SHA256 manifests are checked before execution.
CPU calculations require Python 3.12, NumPy and SciPy; plotting additionally
uses Matplotlib, Pillow and Arial (legacy plots). Final Figure 1 uses DejaVu
Sans distributed with Matplotlib.

| Command | Manuscript evidence |
|---|---|
| `python reproducibility_bundle/portable_reanalysis.py reproducibility_bundle` | Original main Table 4; S1 A-C; historical discovery and pilot/main contrasts |
| `python rerun_additional_analysis.py` | Original diagnostic contrasts, selectors, overlap, planning margins |
| `python verify_additional_analysis.py` | Independent verification of those diagnostics |
| `python reproduce_added_analyses.py` | Main Table 7; S1 input/organ controls, spatial and multiplicity diagnostics |
| `python window_audit_20261019/analyze_windows.py` | Completed nine-window matrix and S1 V-W |
| `python window_audit_20261019/review_checks.py` | Complete-grid technical and row-level checks |
| `python window_audit_20261019/verify_windows.py` | Independent complete-grid calculations |
| `python review_extension_20261019/analyze_extension.py` | Main Table 5 exact all-eight comparison; S1 Y |
| `python review_extension_20261019/verify_extension.py` | Independent all-eight and capture checks |
| `python content_checks_20261019/analyze_content.py` | S1 Z, partial capture, rank expectations, crop multiplicity |
| `python content_checks_20261019/verify_content.py` | Independent rank and paired-ratio checks |
| `python revision_2026_analyses/portable_reproduce.py` | S1.1-S1.3, frozen baseline-margin results and exact identities |
| `python final_resources/compute_error_conditioned.py` | Error-conditioned correction rates across all 16 strata |
| `python current_figures/build_figures.py` | Figures 2-4 and Figure S1 (archived source names Fig2-Fig5) |
| `python final_resources/create_figure1.py` | Final Figure 1 (written to final_resources/figures/) |

S1.4 repeats the full organ-recognition methods/results from the additional
controls. The final descriptive rates divide the frozen stratum rescue counts
by baseline errors; `final_resources/error_conditioned_rescue.json` contains
all counts and fractions. These are new descriptive calculations on existing
predictions, not new inference.

Legacy figure file labels and archive READMEs remain historical records.
For the present manuscript, replace legacy Figure 1 with the final schematic
and relabel legacy Figure 5 as Figure S1. Legacy reconstruction wrappers may
create aliases to original raw paths after checking their hashes.

GPU inference: acquire the exact dataset/model revisions recorded in S1 and
the protocols, reconstruct upstream text using the included utility, adapt
the archived machine-specific paths in a separate copy, and record a new
protocol. Do not overwrite the frozen prediction or protocol records.
