# Oracle headroom and SigLIP crop-ranking benefit on PMC-VQA

Numerical data and reproducible analyses for *Oracle headroom and SigLIP
crop-ranking benefit diverge in Qwen3-VL on PMC-VQA*.

**Archived release v1.0.0:** [10.5281/zenodo.23492663](https://doi.org/10.5281/zenodo.23492663).
The Zenodo archive and GitHub release asset contain the identical verified
`public_data_and_code_v1.0.0.zip` (56,377,051 bytes; SHA256
`b331e5a97d144b88679ac0c3db2a74e3f4f73834e813e3df458cf409e69d93c0`).
The archive was frozen before DOI issuance; this repository's citation metadata
adds the issued DOI without changing the numerical archives.

**Authors:** Nam-Hyun Yoo (Kyungnam University), Hyojin Park (GIIC, Kyungnam
University), Jinhong Yang (Inje University; corresponding author,
jinhong@inje.ac.kr).

The primary cohort contains 2,048 article-linked groups and the separate
curated cohort 825 groups. Both frozen Qwen3-VL model sizes answer the same
questions. The prespecified primary 2B guided-minus-control oracle difference
is -0.15 percentage points (95% CI -0.81 to 0.52). Primary 4B has a small
positive increment; all outcomes, including negative results, are retained.
Oracle candidate coverage, matched crop-ranking increment and executable
decision accuracy are distinct endpoints.

## Contents

- `archives/S2` through `S10`: byte-preserved numerical releases, protocols,
  prediction probabilities, source identifiers, reference mappings, code and
  provenance. SHA256 values are in `SHA256SUMS.json`.
- `final_resources`: final Figure 1 code, exact error-conditioned correction
  rates, and current reproduction resources.
- `REPRODUCING.md`: command-to-result map for all analysis families.
- `verify_and_extract.py`: validates all archive hashes, safely extracts into
  a new directory, and optionally runs the complete CPU reanalysis sequence.

## Quick start

Use Python 3.12 and install `requirements.txt`. From this repository:

```
python verify_and_extract.py --destination reproduction
python verify_and_extract.py --destination reproduction_full --run
```

The destination must not already exist. The second command validates and
reanalyses released predictions; it does not download images or run a model.
It writes per-command logs and a completion receipt inside the destination.
Full historical inference requires the pinned upstream assets and the GPU
environment recorded in the archived protocols.

The original local freezes and original estimates remain unchanged. Statements
in archived READMEs such as "not publicly deposited", "author input required"
or "current figures" describe those earlier local releases. This repository's
root documentation supersedes their publication and figure-version status.
The final Figure 1 source is in `final_resources`; S8 supplies Figures 2-4 and
the original Figure 5 now designated Figure S1.

## Sources and rights

PMC-VQA: https://huggingface.co/datasets/RadGenome/PMC-VQA
(revision b56ae594f794867893143b337b4118a835794647).
SLAKE: https://huggingface.co/datasets/BoKelvin/SLAKE
(revision a9083ce6c34ac3ffb17671a605962924d8a8f9e9).
Original source identifiers, model revisions and reconstruction instructions
are included in the numerical archives. No image collection or model weights
are redistributed. See `LICENSE.txt` for study-material licences and
third-party exceptions.

OpenAI Codex assisted code development and execution, analysis checking,
documentation and plotting. Frozen Qwen models produced the answer records.
