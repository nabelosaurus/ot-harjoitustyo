import unittest
from initialize_database import initialize_database
from database_connection import get_database_connection
from entities.login import Login
from repositories.login_repository import LoginRepository
from services.logins_service import LoginService


class TestLogins(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.login_service = LoginService()

    def test_login_entity_without_username_and_email(self):
        login = Login(
            None,
            "hello",
            "secret"
        )
        self.assertEqual(login.id, None)
        self.assertEqual(login.website, "hello")
        self.assertEqual(login.password, "secret")
        self.assertEqual(login.username, None)
        self.assertEqual(login.email, None)

    def test_login_entity_with_username_and_email(self):
        login = Login(
            None,
            "hello",
            "secret",
            "name",
            "mail"
        )
        self.assertEqual(login.id, None)
        self.assertEqual(login.website, "hello")
        self.assertEqual(login.password, "secret")
        self.assertEqual(login.username, "name")
        self.assertEqual(login.email, "mail")

    def test_validation_10_characters_long_every_field(self):
        login = Login(
            None,
            "hellohello",
            "hellohello",
            "hellohello",
            "hellohello"
        )
        self.assertTrue(self.login_service.validate_input(login))

    def test_validation_5_characters_long_every_field(self):
        login = Login(
            None,
            "hello",
            "hello",
            "hello",
            "hello"
        )
        self.assertFalse(self.login_service.validate_input(login))

    def test_validation_10_characters_long_missing_username_and_email(self):
        login = Login(
            None,
            "hellohello",
            "hellohello"
        )
        self.assertFalse(self.login_service.validate_input(login))

    def test_validation_10_characters_long_missing_username_or_email(self):
        login = Login(
            None,
            "hellohello",
            "hellohello",
            "hellohello"
        )
        self.assertTrue(self.login_service.validate_input(login))

    def tearDown(self):
        initialize_database()
