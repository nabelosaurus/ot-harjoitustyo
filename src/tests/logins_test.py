import unittest
from initialize_database import initialize_database
from database_connection import get_database_connection
from entities.login import Login
from repositories.login_repository import LoginRepository
from services.logins_service import LoginService
from services.validation_service import validate_input


class TestLogins(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.login_service = LoginService()
        self.validate_input = validate_input

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
            "salty",
            "name",
            "mail"
        )
        self.assertEqual(login.id, None)
        self.assertEqual(login.website, "hello")
        self.assertEqual(login.password, "secret")
        self.assertEqual(login.salt, "salty")
        self.assertEqual(login.username, "name")
        self.assertEqual(login.email, "mail")

    def test_validation_10_characters_long_every_field(self):
        login = Login(
            None,
            "hellohello",
            "hellohello",
            "hellohello",
            "hellohello",
            "hellohello"
        )
        self.assertTrue(self.validate_input(login))

    def test_validation_5_characters_long_every_field(self):
        login = Login(
            None,
            "hello",
            "hello",
            "hello",
            "hello",
            "hello"
        )
        self.assertTrue(self.validate_input(login))

    def test_validation_10_characters_long_missing_username_and_email(self):
        login = Login(
            None,
            "hellohello",
            "hellohello"
            "hellohello"
        )
        self.assertTrue(self.validate_input(login))

    def test_validation_10_characters_long_missing_username_or_email(self):
        login = Login(
            None,
            "hellohello",
            "hellohello",
            "hellohello",
            "hellohello"
        )
        self.assertTrue(self.validate_input(login))

    def tearDown(self):
        initialize_database()
