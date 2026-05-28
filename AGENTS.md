# Agent Instructions

This repository is a synthetic-data demo. Do not introduce real customer data, real portfolio data, real people, emails, phone numbers, tokens, secrets, private keys, or employer-internal references.

Generated artifacts must include a visible synthetic-data caveat and must be reproducible from the scripts in `scripts/`.

Before publishing or pushing, audit every file for sensitive content and confirm the demo behavior:

- 30 synthetic positions exist in `Positions_Raw`.
- `AGRD` and `AGRD-CNV` share `canonical_issuer_id` `ISS-104`.
- `ISS-104` aggregate gross exposure is above its issuer limit.
- Every `source_ids` value maps to `Source_Links_Raw`.
- The historical CSV contains 210 data rows.
