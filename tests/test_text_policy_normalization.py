import unittest


from tools.text_policy_normalization import normalize_for_policy_match

class TestTextPolicyNormalization(unittest.TestCase):

    def test_nfkc_and_casefold(self):
        self.assertEqual(normalize_for_policy_match("ＨＥＬＬＯ"), "hello")

    def test_paragraph_whitespace(self):
        self.assertEqual(normalize_for_policy_match("  THE PATIENT    reports a HEADACHE.\nFollow-up is   scheduled for MONDAY.  "),"the patient reports a headache. follow-up is scheduled for monday.")
