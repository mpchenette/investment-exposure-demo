from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

from demo_data import CAVEAT


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "investment_committee_memo_synthetic.pdf"


def build_pdf(path=OUTPUT):
    doc = SimpleDocTemplate(str(path), pagesize=letter, rightMargin=0.7 * inch, leftMargin=0.7 * inch)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Synthetic Investment Committee Market Context Memo", styles["Title"]))
    story.append(Spacer(1, 0.12 * inch))
    story.append(Paragraph(CAVEAT, styles["BodyText"]))
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("Purpose", styles["Heading2"]))
    story.append(
        Paragraph(
            "This memo gives review criteria and market context for a synthetic exposure review packet. "
            "It intentionally avoids stating the conclusion; the workbook data should drive the issuer-level finding.",
            styles["BodyText"],
        )
    )
    story.append(Spacer(1, 0.12 * inch))
    story.append(Paragraph("Review Criteria", styles["Heading2"]))
    criteria = [
        ["Criterion", "Synthetic review action"],
        ["Issuer aggregation", "Aggregate gross exposure by canonical issuer ID before comparing with limits."],
        ["Single-row checks", "Do not rely only on individual ticker exposure when related instruments exist."],
        ["Source mapping", "Confirm every source ID maps to a public or synthetic source reference."],
        ["Trend context", "Use historical snapshots to identify recent concentration changes."],
    ]
    table = Table(criteria, colWidths=[1.8 * inch, 4.7 * inch])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F4E78")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ]
        )
    )
    story.append(table)
    story.append(Spacer(1, 0.18 * inch))
    story.append(Paragraph("Market Context", styles["Heading2"]))
    story.append(
        Paragraph(
            "Synthetic rate, energy, and public filing references are included to resemble a real review packet. "
            "The synthetic scenario assumes higher financing sensitivity for convertible and infrastructure-linked positions.",
            styles["BodyText"],
        )
    )
    story.append(Spacer(1, 0.12 * inch))
    story.append(Paragraph("Source References", styles["Heading2"]))
    story.append(
        Paragraph(
            "Public references used as placeholders: SEC EDGAR, FRED DGS10, EIA STEO, and SEC IAPD. "
            "The memo itself is generated locally and contains only synthetic narrative content.",
            styles["BodyText"],
        )
    )

    doc.build(story)
    return path


if __name__ == "__main__":
    print(build_pdf())
