import unittest
from entities.login import Login
from services.validation_service import validate_input


class TestLogins(unittest.TestCase):
    def setUp(self):
        self.login = Login(None, "http://www.github.com", "password")

    def test_validation_fails_when_only_website_and_password_present(self):
        self.assertFalse(validate_input(self.login)[0])

    def test_validation_fails_when_only_website_password_salt_present(self):
        self.login.salt = "foofoofoofoofoof"
        self.assertFalse(validate_input(self.login)[0])

    def test_validation_fails_when_no_salt_present(self):
        self.login.username = "username"
        self.login.email = "email@email.com"
        self.assertFalse(validate_input(self.login)[0])

    def test_validation_ok_when_website_password_username_email_salt_present(self):
        self.login.username = "username"
        self.login.email = "email@email.com"
        self.login.salt = "foofoofoofoofoof"
        self.assertTrue(validate_input(self.login)[0])

    def test_validation_ok_when_website_password_username_salt_present(self):
        self.login.username = "username"
        self.login.salt = "foofoofoofoofoof"
        self.assertTrue(validate_input(self.login)[0])

    def test_validation_ok_when_website_password_email_salt_present(self):
        self.login.email = "email@email.com"
        self.login.salt = "foofoofoofoofoof"
        self.assertTrue(validate_input(self.login)[0])

    def tearDown(self):
        pass
