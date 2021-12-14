import os
from entities.login import Login
from database_connection import get_database_connection
from repositories.login_repository import LoginRepository
from services.validation_service import validate_input


class LoginService:

    def __init__(self):
        self.login_repository = LoginRepository(get_database_connection())

    def get_all_logins(self):
        return self.login_repository.find_all()

    def create_new(self, details):
        return self.login_repository.create(details)

    def update_existing(self, details):
        return self.login_repository.update_by_id(details)

    def create_login_object(self, website, username, email, password, _id=None):
        return Login(
            _id=_id,
            website=website,
            email=email,
            username=username,
            password=password,
            salt=os.urandom(16)
        )

    def process_save(self, website, username, email, password):
        login = self.create_login_object(website, username, email, password)
        is_valid, error_msg = validate_input(login)
        if is_valid:
            self.create_new(login)
            return True, error_msg
        return False, error_msg


    def process_update(self, login_id, website, email, username, password):
        login = self.create_login_object(website, username, email, password, _id=login_id)
        is_valid, error_msg = validate_input(login)
        if is_valid:
            self.update_existing(login)
            return True, error_msg
        return False, error_msg