import unittest
from registration import check_password_length, passwords_match, is_registered, register

from initialize_database import initialize_database
from entities.user import User
from repositories.user_repository import UserRepository
from database_connection import get_database_connection


class TestRegister(unittest.TestCase):
    def setUp(self):
        initialize_database()

    def test_check_password_length_with_password_thats_too_short(self):
        self.assertFalse(check_password_length("password"))

    def test_check_password_length_with_password_that_meets_length_requirements(self):
        self.assertTrue(check_password_length("passwordpassword"))

    def test_check_non_matching_passwords(self):
        self.assertFalse(passwords_match("password", "verification"))

    def test_check_matching_passwords(self):
        self.assertTrue(passwords_match(
            "passwordpassword", "passwordpassword"))

    def test_check_that_user_is_registered(self):
        self.assertFalse(is_registered())

    def test_check_that_user_is_registered(self):
        user_repository = UserRepository(get_database_connection())
        user_repository.create(User(_id=None, master_password="hello"))
        self.assertTrue(is_registered())

    def test_check_multiple_users_registered(self):
        user_repository = UserRepository(get_database_connection())
        user_repository.create(User(_id=None, master_password="hello"))
        user_repository.create(User(_id=None, master_password="hello2"))
        user_repository.create(User(_id=None, master_password="hello3"))
        self.assertTrue(is_registered())

    def test_registration_possible_when_password_criteria_met(self):
        self.assertTrue(register("hellohello", "hellohello"))

    def test_registration_not_possible_when_password_and_verification_differ(self):
        self.assertFalse(register("hellohello", "olleholleh"))

    def test_registration_not_possible_when_password_too_short(self):
        self.assertFalse(register("hello", "hello"))

    def test_registration_not_possible_when_parameters_empty(self):
        self.assertFalse(register("", ""))


    def tearDown(self):
        initialize_database()
