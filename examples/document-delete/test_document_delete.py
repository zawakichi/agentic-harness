import unittest
from document_delete import Actor, delete_document


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.docs = {"a": "A", "b": "B", "c": "A"}

    def test_001_admin_can_delete_own_document(self):
        self.assertEqual(delete_document(Actor("A", True), "a", self.docs),
                         ("DELETED", {"b": "B", "c": "A"}))
        self.assertEqual(self.docs, {"a": "A", "b": "B", "c": "A"})

    def test_002_other_tenant_denied(self):
        self.assertEqual(delete_document(Actor("A", True), "b", self.docs), ("DENIED", self.docs))

    def test_003_non_admin_denied(self):
        self.assertEqual(delete_document(Actor("A", False), "a", self.docs), ("DENIED", self.docs))

    def test_004_missing_document(self):
        self.assertEqual(delete_document(Actor("A", True), "missing", self.docs), ("NOT_FOUND", self.docs))

    def test_invariant_001_exhaustive_over_example_domain(self):
        for tenant in ("A", "B", "C"):
            for admin in (True, False):
                for doc, owner in self.docs.items():
                    result, after = delete_document(Actor(tenant, admin), doc, self.docs)
                    allowed = admin and tenant == owner
                    self.assertEqual(result == "DELETED", allowed)
                    self.assertEqual(after, {k: v for k, v in self.docs.items() if not (allowed and k == doc)})
