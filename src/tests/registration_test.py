import unittest
from registration import check_password_length, passwords_match

class TestRegister(unittest.TestCase):
    def setUp(self):
        pass

    def test_check_password_length_with_password_thats_too_short(self):
        self.assertFalse(check_password_length("password"))

    def test_check_password_length_with_password_that_meets_length_requirements(self):
        self.assertTrue(check_password_length("passwordpassword"))

    def test_check_non_matching_passwords(self):
        self.assertFalse(passwords_match("password", "verification"))

    def test_check_matching_passwords(self):
        self.assertTrue(passwords_match("passwordpassword", "passwordpassword"))

    def tearDown(self):
        pass
