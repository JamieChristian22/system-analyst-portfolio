#!/usr/bin/env python3
"""Offline contract checks for the simulated appointment-system portfolio.

Checks written requirement artifacts only. This does not run an appointment
service, check native spreadsheet traceability, or verify real patient outcomes.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCUMENTS = {
    "BR": "Requirements_Documentation/01_Business_Requirements_Document.md",
    "FR": "Requirements_Documentation/02_Functional_Requirements_Specification.md",
    "NFR": "Data_Security_NFR/05_Nonfunctional_Requirements_Matrix.md",
    "DV": "Data_Security_NFR/04_Data_Validation_Rules.md",
}
CODE = re.compile(r"^(BR|FR|NFR|DV)-(\d{3})$")


def rows(markdown: str, prefix: str) -> list[list[str]]:
    found = []
    for line in markdown.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and CODE.fullmatch(cells[0]) and cells[0].startswith(prefix + "-"):
            found.append(cells)
    return found


def check(requirements: dict[str, str]) -> dict:
    errors = []
    totals = {}
    for kind in DOCUMENTS:
        collected = rows(requirements[kind], kind)
        numbers = [int(c[0].split("-")[1]) for c in collected]
        if not numbers:
            errors.append(f"{kind}: no requirements found")
        if len(numbers) != len(set(numbers)):
            errors.append(f"{kind}: duplicate IDs")
        if sorted(numbers) != list(range(1, len(numbers) + 1)):
            errors.append(f"{kind}: IDs are not contiguous from 001")
        for row in collected:
            if len(row) != 4 or not all(row[:4]):
                errors.append(f"{row[0]}: missing table fields")
            if kind == "BR" and len(row) == 4 and row[2] not in {"Must", "Should", "Could", "Won't"}:
                errors.append(f"{row[0]}: unexpected requirement priority")
        totals[kind] = len(collected)
    fr_rows = rows(requirements["FR"], "FR")
    uat = [r[3] for r in fr_rows if len(r) > 3]
    if len(set(uat)) != len(uat):
        errors.append("FR: duplicate UAT mapping")
    if any(not re.fullmatch(r"UAT-\d{2}", value) for value in uat):
        errors.append("FR: invalid UAT mapping format")
    return {
        "status": "PASS" if not errors else "FAIL",
        "requirement_counts": totals,
        "functional_to_uat_references": len(uat),
        "limitations": (
            "Checks Markdown IDs, table fields and declared FR/UAT labels; "
            "does not independently inspect Excel UAT cases or confirm software behavior."
        ),
        "errors": errors,
    }


def validate(root: Path = ROOT) -> dict:
    documents = {kind: (root / path).read_text(encoding="utf-8")
                 for kind, path in DOCUMENTS.items()}
    report = check(documents)
    api = (root / "System_Analysis_Integration/02_API_Requirements_Specification.md").read_text(encoding="utf-8")
    examples = re.findall(r"```json\s*(.*?)\s*```", api, flags=re.S | re.I)
    if len(examples) < 2:
        report["errors"].append("API: expected request and response JSON examples")
    else:
        for i, sample in enumerate(examples, 1):
            try:
                json.loads(sample)
            except json.JSONDecodeError as exc:
                report["errors"].append(f"API: invalid JSON example {i}: {exc}")
    report["api_json_examples_checked"] = len(examples)
    report["status"] = "FAIL" if report["errors"] else "PASS"
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "reports/requirements-validation.json")
    args = parser.parse_args()
    try:
        report = validate()
    except (OSError, UnicodeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
