# MPC Investment Exposure Demo

This repository is a fully synthetic, public-safe demo for a Codex CLI workflow. It models a source-controlled data-production pipeline behind an investment exposure review packet.

The demo flow is:

1. Generate a deterministic workbook, historical CSV, and market-context PDF.
2. Inspect the generated artifacts for a possible issuer-level concentration issue.
3. Validate that the generated packet was produced from local scripts and source files.

All issuer names, positions, committee notes, and exposure numbers are synthetic. This repository contains no real customer data, portfolio data, people, emails, phone numbers, tokens, secrets, or employer-internal references.

## Generated Artifacts

The generated artifacts are intentionally ignored by git:

- `exposure_review_packet_synthetic.xlsx`
- `historical_exposure_snapshots_2026-Q2.csv`
- `investment_committee_memo_synthetic.pdf`

Recreate them with:

```bash
python scripts/generate_exposure_workbook.py
python scripts/generate_historical_snapshots.py
python scripts/generate_market_context_memo_pdf.py
```

## Demo Finding

The workbook includes 30 synthetic positions. Two positions share the same canonical issuer:

- `AGRD`, Aurora Grid Systems, `ISS-104`, gross exposure `9.1`, issuer limit `10.0`
- `AGRD-CNV`, Aurora Grid Systems 2029 Convertible, `ISS-104`, gross exposure `6.1`, issuer limit `10.0`

Each row appears below the issuer limit on its own, but the issuer-level aggregate is `15.2`, which exceeds the `10.0` limit and should be reviewed.

## Verification

Run the export-quality checks with:

```bash
python tests/test_export_quality.py
```

The test regenerates missing artifacts and asserts that the workbook, CSV, source mapping, and issuer-level concentration behavior match the intended demo.
