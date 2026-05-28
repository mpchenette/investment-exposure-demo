# Data Lineage

All generated outputs are built from deterministic synthetic records in `scripts/demo_data.py`.

## Pipeline

1. `scripts/demo_data.py` defines synthetic positions, source references, data dictionary entries, and historical as-of dates.
2. `scripts/generate_exposure_workbook.py` writes the review workbook and computes issuer aggregates.
3. `scripts/generate_historical_snapshots.py` writes seven weekly snapshots for all 30 positions.
4. `scripts/generate_market_context_memo_pdf.py` writes a synthetic committee memo with market context and review criteria.
5. `tests/test_export_quality.py` regenerates missing artifacts and validates the expected demo behavior.

## Public-Safety Controls

- No external systems are queried.
- No random data is used.
- All names, notes, identifiers, and numbers are synthetic.
- Source links point to public reference locations or the synthetic memo filename.
