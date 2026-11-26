# A refined BMV lower bound for three-dimensional Hamiltonians

**Chain.Ren · Independent research · 2026-11-27**

The normalized trace average of words with three copies of one positive semidefinite matrix and five through nine copies of another dominates the corresponding evenly spread word in dimension three. For exponentials of Hermitian matrices this gives the refined BMV partition-function lower bound. The first case is identified in [Hägele's §7](https://arxiv.org/html/2611.00129v1).

[Complete proof and coefficient table](PROOF.md) · [Verification script](verify.py) · [Version](https://github.com/Asakitan/refined-bmv-three-by-three/releases/tag/proof-v1.0.1) · [Citation](CITATION.cff) · [Prior work](SOURCES.md)

Run `python -B verify.py` (Python 3.9+, standard library) to reconstruct the five integer polynomials and check all coefficients. The hypotheses include noncommuting matrices; matrices of dimension greater than three are not covered.
