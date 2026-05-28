from __future__ import annotations

import csv
from pathlib import Path

from demo_data import POSITION_COLUMNS, historical_positions


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "historical_exposure_snapshots_2026-Q2.csv"


def build_csv(path=OUTPUT):
    rows = historical_positions()
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=POSITION_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    return path


if __name__ == "__main__":
    print(build_csv())
