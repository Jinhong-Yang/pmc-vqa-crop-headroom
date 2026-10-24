# Oracle headroom and SigLIP crop-ranking benefit on PMC-VQA

Complete numerical data and reproducible analyses for *Oracle headroom and SigLIP crop-ranking benefit diverge in Qwen3-VL on PMC-VQA*.

**Current complete release: version 1.1.0**, DOI [10.5281/zenodo.23614485](https://doi.org/10.5281/zenodo.23614485). This release contains every numerical archive S2-S13. Earlier version 1.0.0 remains at [10.5281/zenodo.23492663](https://doi.org/10.5281/zenodo.23492663); original archived files are preserved.

Authors: Nam-Hyun Yoo (Kyungnam University), Hyojin Park (GIIC, Kyungnam University), Jinhong Yang (Inje University; corresponding author, jinhong@inje.ac.kr).

## Study and extensions

The original primary cohort contains 2,048 article-linked groups and the separate curated cohort 825 groups. Frozen Qwen3-VL 2B and 4B answer the same questions. The locally prespecified, hash-locked primary 2B guided-minus-control two-candidate oracle difference is -0.15 percentage points (95% CI -0.81 to 0.52). The primary 4B positive estimate is nominal and exploratory. Local freezes are not external registration.

The first 24 October extension (S12) adds a non-visual choice-order perturbation. It produced 13.04 pp of headroom, compared with 4.93 for guided crops. Their cross-intervention difference is 8.11 pp (95% CI 6.45 to 9.77); candidate type and image-token budgets differ, so this is not a matched ranking contrast. The extension also includes smaller-window pilot, fixed-position comparisons and calibration.

The second 24 October extension (S13) averages probabilities over four cyclic option orders within each of five conditions, after restoring option identities. The primary 2B matched contrast becomes +0.98 pp (nominal 95% CI +0.26 to +1.71). Original baseline and averaged baseline direct accuracies are 43.26% and 45.80%. This is probability averaging before choosing an answer, not an oracle across order-specific answers. Each option occupies each letter once, but only four of 24 permutations are evaluated. All 2,048 main questions follow a 128-question technical pilot. No efficacy-based exclusions or stopping were used.

The positive averaged oracle increment qualifies the original near-zero result: the ranking estimate depends on option-order handling. Averaged guided and baseline direct accuracy were both 45.80%, with 106 rescues and 106 harms. The guided-minus-control direct difference was +0.55 pp (nominal 95% CI -0.44 to +1.55). No general absence of ranking benefit or direct-accuracy improvement is established. This extension is exploratory and leaves the original primary analysis intact.

## Contents and reproduction

- archives/S2-S10: original numerical releases, hashes, source identifiers and executable analyses.
- archives/S11_File.zip: standalone original final resources, unchanged.
- archives/S12_presentation_and_selector_controls.zip: first 24 October extension, unchanged.
- archives/S13_order_averaging_and_diagnostics.zip: new raw probabilities, complete mappings, protocol/gates, counts, statistics and independent CPU verification.
- current_release_figures/: current manuscript artwork and portable current Figure 1/S2 source code; Figure S2 has no planning-range band. Figures 2,3 and S1 are unchanged.
- SHA256SUMS.json: archive hashes. REPRODUCING.md: command map. verify_and_extract.py: verify and safely extract all archives to one fresh folder; optionally run the full numerical sequence.

After common extraction, the new extension runs with Python and NumPy:

    python order_averaging_20261024/reproduce_release.py

This checks raw-to-compact mappings, counts, probability averages, all paired bootstrap intervals, letter-position counts and baseline runner-up transitions. It does not need internet access, images or model weights. The original full pipeline additionally requires SciPy, Matplotlib, Pillow and the documented Arial font for legacy plots.

## Source rights and scope

No original biomedical image pixels, source question/option text, model weights or private patient records are redistributed. Pinned upstream sources and reconstruction instructions are in the numerical archives. Source images and text remain subject to their original terms. No clinician label/relevance annotation audit or larger-model experiment is claimed. All new analyses are exploratory.

Study-generated numerical data, documentation and figures: CC BY 4.0. Study-authored code: MIT. Third-party notices retain their original rights; see LICENSE.txt. OpenAI Codex assisted implementation, execution, numerical checks, documentation and plotting; the experimental answer records are actual frozen-model inference outputs.

Historical READMEs inside the preserved archives describe their original releases. This root documentation controls the current release and figure mapping. Current manuscript tables are: primary contrast Table 4, complete grid Table 5, image controls Table 6, derangement Table 7, and four-order sensitivity Table 8. The complete current S1 table mapping is in the submission draft.
