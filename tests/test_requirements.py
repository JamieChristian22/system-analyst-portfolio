"""Negative-case tests for requirements and functional-to-UAT traceability."""
import unittest
from tools.validate_requirements import DOCUMENTS, check, rows, validate, ROOT


class RequirementsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.docs = {kind: (ROOT / path).read_text(encoding="utf-8")
                    for kind, path in DOCUMENTS.items()}

    def test_existing_contracts_have_no_errors(self):
        report = validate()
        self.assertEqual(report["status"], "PASS", report["errors"])
        self.assertEqual(report["requirement_counts"], {"BR": 10, "FR": 16, "NFR": 12, "DV": 10})
        self.assertEqual(report["functional_to_uat_references"], 16)
        self.assertEqual(report["api_json_examples_checked"], 2)

    def test_duplicate_fr_id_rejected(self):
        docs = dict(self.docs)
        original = rows(docs["FR"], "FR")
        self.assertTrue(original)
        docs["FR"] += "\n| " + " | ".join(original[0]) + " |\n"
        self.assertTrue(any("duplicate" in e for e in check(docs)["errors"]))

    def test_gap_in_business_requirement_ids_rejected(self):
        docs = dict(self.docs)
        docs["BR"] = docs["BR"].replace("| BR-005 |", "| BR-099 |")
        self.assertTrue(any("not contiguous" in e for e in check(docs)["errors"]))

    def test_unmapped_functional_requirement_rejected(self):
        docs = dict(self.docs)
        docs["FR"] = docs["FR"].replace("| UAT-05 |", "| not-mapped |")
        self.assertTrue(any("invalid UAT" in e for e in check(docs)["errors"]))

    def test_duplicate_uat_mapping_rejected(self):
        docs = dict(self.docs)
        docs["FR"] = docs["FR"].replace("| UAT-06 |", "| UAT-05 |")
        self.assertTrue(any("duplicate UAT" in e for e in check(docs)["errors"]))

    def test_invalid_priority_rejected(self):
        docs = dict(self.docs)
        docs["BR"] = docs["BR"].replace("| Must |", "| Mystery |", 1)
        self.assertTrue(any("priority" in e for e in check(docs)["errors"]))


if __name__ == "__main__":
    unittest.main()
