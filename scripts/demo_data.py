from __future__ import annotations

from copy import deepcopy
from datetime import date, timedelta


CAVEAT = "SYNTHETIC DATA DEMO: no real customer, portfolio, person, email, phone, token, secret, or internal data."
PORTFOLIO_ID = "SYNTH-CORE-01"
AS_OF_DATE = date(2026, 6, 26)

POSITION_COLUMNS = [
    "as_of_date",
    "portfolio_id",
    "ticker",
    "instrument_name",
    "asset_class",
    "sector",
    "issuer",
    "canonical_issuer_id",
    "quantity",
    "price",
    "market_value",
    "gross_exposure",
    "issuer_limit",
    "currency",
    "source_ids",
    "is_synthetic",
]

SOURCE_LINKS = [
    {
        "source_id": "SEC_EDGAR",
        "source_name": "SEC EDGAR public company search",
        "source_type": "public_reference",
        "location": "https://www.sec.gov/edgar/search/",
        "usage": "Public filings reference context for demo workflow.",
    },
    {
        "source_id": "FRED_DGS10",
        "source_name": "FRED DGS10 Treasury series",
        "source_type": "public_reference",
        "location": "https://fred.stlouisfed.org/series/DGS10",
        "usage": "Rates context for synthetic memo.",
    },
    {
        "source_id": "EIA_STEO",
        "source_name": "EIA Short-Term Energy Outlook",
        "source_type": "public_reference",
        "location": "https://www.eia.gov/outlooks/steo/",
        "usage": "Energy market context for synthetic memo.",
    },
    {
        "source_id": "SEC_IAPD",
        "source_name": "SEC adviser public disclosure",
        "source_type": "public_reference",
        "location": "https://adviserinfo.sec.gov/",
        "usage": "Public diligence reference for demo source review.",
    },
    {
        "source_id": "SYNTH_MEMO",
        "source_name": "Synthetic internal committee memo",
        "source_type": "generated_synthetic_document",
        "location": "investment_committee_memo_synthetic.pdf",
        "usage": "Synthetic market narrative and review criteria.",
    },
]

DATA_DICTIONARY = [
    ("as_of_date", "Snapshot date for the synthetic position record."),
    ("portfolio_id", "Synthetic portfolio identifier."),
    ("ticker", "Synthetic ticker or instrument code."),
    ("instrument_name", "Synthetic instrument display name."),
    ("asset_class", "Synthetic asset class grouping."),
    ("sector", "Synthetic sector grouping."),
    ("issuer", "Synthetic issuer display name."),
    ("canonical_issuer_id", "Normalized synthetic issuer identifier used for aggregation."),
    ("quantity", "Synthetic quantity."),
    ("price", "Synthetic unit price."),
    ("market_value", "Synthetic market value."),
    ("gross_exposure", "Synthetic gross exposure as a percent of portfolio gross exposure."),
    ("issuer_limit", "Synthetic issuer-level review limit."),
    ("currency", "Synthetic reporting currency."),
    ("source_ids", "Pipe-delimited source identifiers mapped to Source_Links_Raw."),
    ("is_synthetic", "Always true for this public-safe demo."),
]


def _row(ticker, name, asset_class, sector, issuer, issuer_id, exposure, source_ids, idx):
    quantity = 1000 + idx * 75
    price = round(20 + idx * 1.35, 2)
    return {
        "as_of_date": AS_OF_DATE.isoformat(),
        "portfolio_id": PORTFOLIO_ID,
        "ticker": ticker,
        "instrument_name": name,
        "asset_class": asset_class,
        "sector": sector,
        "issuer": issuer,
        "canonical_issuer_id": issuer_id,
        "quantity": quantity,
        "price": price,
        "market_value": round(quantity * price, 2),
        "gross_exposure": exposure,
        "issuer_limit": 10.0,
        "currency": "USD",
        "source_ids": source_ids,
        "is_synthetic": True,
    }


def positions():
    rows = [
        _row("AGRD", "Aurora Grid Systems Common", "Equity", "Utilities", "Aurora Grid Systems", "ISS-104", 9.1, "SEC_EDGAR|SYNTH_MEMO", 1),
        _row("AGRD-CNV", "Aurora Grid Systems 2029 Convertible", "Convertible", "Utilities", "Aurora Grid Systems 2029 Convertible", "ISS-104", 6.1, "SEC_EDGAR|FRED_DGS10|SYNTH_MEMO", 2),
        _row("BLUM", "Blue Meridian Industrials", "Equity", "Industrials", "Blue Meridian Works", "ISS-101", 4.2, "SEC_EDGAR", 3),
        _row("CRST", "Crestline Robotics", "Equity", "Technology", "Crestline Robotics", "ISS-102", 3.8, "SEC_EDGAR", 4),
        _row("NOVA", "Novara Foods", "Equity", "Consumer Staples", "Novara Foods", "ISS-103", 2.9, "SEC_EDGAR", 5),
        _row("HARB", "Harborline Freight Notes", "Credit", "Industrials", "Harborline Freight", "ISS-105", 3.4, "FRED_DGS10", 6),
        _row("LUMA", "LumaCare Health", "Equity", "Health Care", "LumaCare Health", "ISS-106", 2.7, "SEC_EDGAR", 7),
        _row("TERR", "TerraPeak Materials", "Equity", "Materials", "TerraPeak Materials", "ISS-107", 3.1, "SEC_EDGAR|EIA_STEO", 8),
        _row("QUAY", "Quaystone REIT", "Equity", "Real Estate", "Quaystone REIT", "ISS-108", 2.5, "SEC_EDGAR", 9),
        _row("PINE", "Pinewell Bank Preferred", "Preferred", "Financials", "Pinewell Bank", "ISS-109", 3.6, "SEC_IAPD|FRED_DGS10", 10),
        _row("SOLR", "Solara Storage", "Equity", "Energy", "Solara Storage", "ISS-110", 2.8, "SEC_EDGAR|EIA_STEO", 11),
        _row("MTRX", "Matrix Harbor Software", "Equity", "Technology", "Matrix Harbor Software", "ISS-111", 3.3, "SEC_EDGAR", 12),
        _row("ORBT", "Orbitelle Media", "Equity", "Communication Services", "Orbitelle Media", "ISS-112", 2.1, "SEC_EDGAR", 13),
        _row("VALE", "Valecrest Pharma", "Equity", "Health Care", "Valecrest Pharma", "ISS-113", 3.0, "SEC_EDGAR", 14),
        _row("RIVR", "Riverbend Water Bonds", "Municipal", "Utilities", "Riverbend Water Authority", "ISS-114", 2.4, "SYNTH_MEMO", 15),
        _row("CIRR", "Cirrus Ferry Holdings", "Equity", "Industrials", "Cirrus Ferry Holdings", "ISS-115", 2.6, "SEC_EDGAR", 16),
        _row("MNTA", "Montara Retail", "Equity", "Consumer Discretionary", "Montara Retail", "ISS-116", 2.2, "SEC_EDGAR", 17),
        _row("VEGA", "VegaChip Design", "Equity", "Technology", "VegaChip Design", "ISS-117", 3.7, "SEC_EDGAR", 18),
        _row("NIMB", "Nimble Rail", "Equity", "Industrials", "Nimble Rail", "ISS-118", 2.3, "SEC_EDGAR", 19),
        _row("KITE", "Kitewell Insurance", "Equity", "Financials", "Kitewell Insurance", "ISS-119", 2.9, "SEC_IAPD", 20),
        _row("FJRD", "Fjordline Data Centers", "REIT", "Real Estate", "Fjordline Data Centers", "ISS-120", 3.5, "SEC_EDGAR|FRED_DGS10", 21),
        _row("EMBER", "Emberfield Midstream", "Equity", "Energy", "Emberfield Midstream", "ISS-121", 2.7, "SEC_EDGAR|EIA_STEO", 22),
        _row("CLOV", "Clovelle Diagnostics", "Equity", "Health Care", "Clovelle Diagnostics", "ISS-122", 2.0, "SEC_EDGAR", 23),
        _row("ATLS", "Atlas Cove Shipping", "Equity", "Industrials", "Atlas Cove Shipping", "ISS-123", 2.8, "SEC_EDGAR", 24),
        _row("MEAD", "Meadowgate Foods", "Equity", "Consumer Staples", "Meadowgate Foods", "ISS-124", 2.5, "SEC_EDGAR", 25),
        _row("PRSM", "PrismWorks Cloud", "Equity", "Technology", "PrismWorks Cloud", "ISS-125", 3.2, "SEC_EDGAR", 26),
        _row("ROAN", "Roanoke Labs", "Equity", "Health Care", "Roanoke Labs", "ISS-126", 2.4, "SEC_EDGAR", 27),
        _row("SILT", "Siltstone Copper", "Equity", "Materials", "Siltstone Copper", "ISS-127", 2.6, "SEC_EDGAR", 28),
        _row("BAYN", "BayNorth Telecom", "Equity", "Communication Services", "BayNorth Telecom", "ISS-128", 2.3, "SEC_EDGAR", 29),
        _row("WIND", "Windmere Renewables", "Equity", "Utilities", "Windmere Renewables", "ISS-129", 2.9, "SEC_EDGAR|EIA_STEO", 30),
    ]
    return deepcopy(rows)


def issuer_aggregates(position_rows=None):
    aggregates = {}
    for row in position_rows or positions():
        issuer_id = row["canonical_issuer_id"]
        item = aggregates.setdefault(
            issuer_id,
            {
                "canonical_issuer_id": issuer_id,
                "issuer": row["issuer"],
                "aggregate_gross_exposure": 0.0,
                "issuer_limit": row["issuer_limit"],
                "tickers": [],
                "review_status": "Within limit",
            },
        )
        item["aggregate_gross_exposure"] = round(item["aggregate_gross_exposure"] + row["gross_exposure"], 2)
        item["tickers"].append(row["ticker"])
    for item in aggregates.values():
        if item["aggregate_gross_exposure"] > item["issuer_limit"]:
            item["review_status"] = "Needs issuer-level review"
        item["tickers"] = ", ".join(item["tickers"])
    return list(aggregates.values())


def historical_positions():
    base_rows = positions()
    start = AS_OF_DATE - timedelta(weeks=6)
    dates = [(start + timedelta(weeks=i)).isoformat() for i in range(7)]
    agrd_path = [4.2, 5.0, 5.8, 6.7, 7.6, 8.4, 9.1]
    cnv_path = [1.0, 1.5, 2.2, 2.9, 3.8, 4.9, 6.1]
    rows = []
    for idx, as_of in enumerate(dates):
        for base in base_rows:
            row = dict(base)
            row["as_of_date"] = as_of
            if row["ticker"] == "AGRD":
                row["gross_exposure"] = agrd_path[idx]
            elif row["ticker"] == "AGRD-CNV":
                row["gross_exposure"] = cnv_path[idx]
            else:
                drift = (idx - 6) * 0.03
                row["gross_exposure"] = round(max(0.5, row["gross_exposure"] + drift), 2)
            row["market_value"] = round(row["market_value"] * (0.985 + idx * 0.0025), 2)
            rows.append(row)
    return rows
