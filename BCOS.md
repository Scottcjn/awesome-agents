# BCOS — Beacon Certified Open Source

[![BCOS Certified](https://img.shields.io/badge/BCOS-Certified-brightgreen?style=flat)](https://rustchain.org/bcos/)

This repository targets certification under the **Beacon Certified Open Source
(BCOS)** program by [Elyan Labs](https://elyanlabs.ai). License: `MIT`.

## Verification
```bash
python3 -m pip install clawrtc
clawrtc bcos scan .
```
Verify at: **[rustchain.org/bcos/](https://rustchain.org/bcos/)**

## What BCOS Certifies
License compliance (SPDX + OSI-compatible), OSV/CVE vuln scan, Semgrep static
analysis, SBOM, dependency freshness, test evidence, and human/agent review
attestation. Trust score 0-100. On-chain BLAKE2b-256 proof anchored to RustChain.

- **Reviewed By**: Scott Boudreaux ([@Scottcjn](https://github.com/Scottcjn))
- **Organization**: [Elyan Labs](https://elyanlabs.ai) · **Chain**: [RustChain](https://rustchain.org)
- **On-Chain Proof**: pending — run `clawrtc bcos scan .` to mint the BCOS id.
