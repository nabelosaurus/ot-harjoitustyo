import unittest
from user_login import login_succesfull
from initialize_database import initialize_database
from entities.user import User
from repositories.user_repository import UserRepository
from database_connection import get_database_connection


class TestUserLogin(unittest.TestCase):
    def setUp(self):
        initialize_database()


    def test_check_login_works_with_one_record_in_database(self):
        user_repository = UserRepository(get_database_connection())
        user_repository.create(User(_id=None, master_password="hello"))
        self.assertTrue(login_succesfull("hello"))

    def test_check_login_works_with_multiple_records_in_database_asc(self):
        user_repository = UserRepository(get_database_connection())
        user_repository.create(User(_id=None, master_password="hello1"))
        user_repository.create(User(_id=None, master_password="hello2"))
        user_repository.create(User(_id=None, master_password="hello3"))
        user_repository.create(User(_id=None, master_password="hello4"))
        user_repository.create(User(_id=None, master_password="hello5"))
        self.assertTrue(login_succesfull("hello1"))

    def test_check_login_works_with_multiple_records_in_database_desc(self):
        user_repository = UserRepository(get_database_connection())
        user_repository.create(User(_id=None, master_password="hello5"))
        user_repository.create(User(_id=None, master_password="hello4"))
        user_repository.create(User(_id=None, master_password="hello3"))
        user_repository.create(User(_id=None, master_password="hello2"))
        user_repository.create(User(_id=None, master_password="hello1"))
        self.assertTrue(login_succesfull("hello5"))
    

    def tearDown(self):
        initialize_database()
