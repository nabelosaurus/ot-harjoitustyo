import os
from entities.login import Login
from database_connection import get_database_connection
from repositories.login_repository import LoginRepository


class LoginService:

    def __init__(self):
        self.login_repository = LoginRepository(get_database_connection())

    def get_all_logins(self):
        return self.login_repository.find_all()

    def create_new(self, details):
        return self.login_repository.create(details)

    def create_login_object(self, website, username, email, password):
        return Login(
            _id=None,
            website=website,
            email=email,
            username=username,
            password=password,
            salt=os.urandom(16)
        )

    def validate_input(self, login):
        valid = True
        if not login.website:
            valid = False
        if not login.password:
            valid = False
        if not login.username and not login.email:
            valid = False
        if len(login.website) < 4:
            valid = False
        if len(login.password) < 1:
            valid = False
        if login.username:
            if 0 < len(login.username) < 2:
                valid = False
        if login.email:
            if 0 < len(login.email) < 8:
                valid = False
        if not login.salt:
            valid = False
        return valid

    def process_save(self, website, username, email, password):
        login = self.create_login_object(website, username, email, password)
        is_valid = self.validate_input(login)
        if is_valid:
            self.create_new(login)
            return True
        return False
