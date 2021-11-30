import unittest
from services.user_service import UserService
from initialize_database import initialize_database
from entities.user import User
from repositories.user_repository import UserRepository
from database_connection import get_database_connection


class TestRegister(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.user_service = UserService()

    def test_check_password_length_with_password_thats_too_short(self):
        self.assertFalse(self.user_service.check_password_length("password"))

    def test_check_password_length_with_password_that_meets_length_requirements(self):
        self.assertTrue(
            self.user_service.check_password_length("passwordpassword"))

    def test_check_non_matching_passwords(self):
        self.assertFalse(self.user_service.passwords_match(
            "password", "verification"))

    def test_check_matching_passwords(self):
        self.assertTrue(self.user_service.passwords_match(
            "passwordpassword", "passwordpassword"))

    def test_check_that_user_is_registered(self):
        self.assertFalse(is_registered())

    def test_check_that_user_is_registered(self):
        user_repository = UserRepository(get_database_connection())
        user_repository.create(User(_id=None, master_password="hello"))
        self.assertTrue(self.user_service.is_registered())

    def test_check_multiple_users_registered(self):
        user_repository = UserRepository(get_database_connection())
        user_repository.create(User(_id=None, master_password="hello"))
        user_repository.create(User(_id=None, master_password="hello2"))
        user_repository.create(User(_id=None, master_password="hello3"))
        self.assertTrue(self.user_service.is_registered())

    def test_registration_possible_when_password_criteria_met(self):
        self.assertTrue(self.user_service.register("hellohello", "hellohello"))

    def test_registration_not_possible_when_password_and_verification_differ(self):
        self.assertFalse(self.user_service.register(
            "hellohello", "olleholleh"))

    def test_registration_not_possible_when_password_too_short(self):
        self.assertFalse(self.user_service.register("hello", "hello"))

    def test_registration_not_possible_when_parameters_empty(self):
        self.assertFalse(self.user_service.register("", ""))

    def tearDown(self):
        initialize_database()
