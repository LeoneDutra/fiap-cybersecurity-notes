"""Generate glossary/GLOSSARY.md (A–Z) from glossary/glossary.csv.

Usage:  python scripts/build_glossary.py
"""

import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "glossary" / "glossary.csv"
OUT = ROOT / "glossary" / "GLOSSARY.md"


def main() -> None:
    with SRC.open(encoding="utf-8") as f:
        rows = sorted(csv.DictReader(f), key=lambda r: r["term_pt"].casefold())

    by_letter: defaultdict[str, list[dict]] = defaultdict(list)
    for row in rows:
        by_letter[row["term_pt"][:1].upper()].append(row)

    lines = [
        "# 📖 Glossary (PT ↔ EN)",
        "",
        "> Generated from `glossary.csv` by `scripts/build_glossary.py`. Edit the CSV, not this file.",
        "",
        f"**{len(rows)} terms**",
        "",
    ]
    if by_letter:
        lines.append(" · ".join(f"[{letter}](#{letter.lower()})" for letter in sorted(by_letter)))
        lines.append("")
    for letter in sorted(by_letter):
        lines += [f"## {letter}", "", "| Termo (PT) | Term (EN) | Categoria | Definição | Fase |",
                  "|---|---|---|---|---|"]
        for r in by_letter[letter]:
            term = r["term_pt"] + (f" ({r['acronym']})" if r["acronym"] else "")
            lines.append(
                f"| **{term}** | {r['term_en']} | {r['category']} | "
                f"{r['definition_pt']} | {r['phases']} |"
            )
        lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} with {len(rows)} terms")


if __name__ == "__main__":
    main()
