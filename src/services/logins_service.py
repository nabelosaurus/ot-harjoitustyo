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

    def validate_input(self, login):
        valid = True
        error_msg = ""
        if not login.website:
            error_msg += "Website must be present. "
            valid = False
        if not login.password:
            error_msg += "Password must be present. "
            valid = False
        if not login.username and not login.email:
            error_msg += "Username and email can not both be empty. "
            valid = False
        if len(login.website) < 4:
            error_msg += "Website length must be greater than four characters. "
            valid = False
        if len(login.password) < 1:
            error_msg += "Password must be atleast one character. "
            valid = False
        if login.username:
            if 0 < len(login.username) < 2:
                print(login.username)
                error_msg += "The username must be longer than 1 character. "
                valid = False
        if login.email:
            if 0 < len(login.email) < 6:
                error_msg += "The email must be longer than 5 characters. "
                valid = False
        if not login.salt:
            valid = False
        return valid, error_msg

    def process_save(self, website, username, email, password):
        login = self.create_login_object(website, username, email, password)
        is_valid, error_msg = self.validate_input(login)
        if is_valid:
            self.create_new(login)
            return True, error_msg
        return False, error_msg


    def process_update(self, login_id, website, email, username, password):
        login = self.create_login_object(website, username, email, password, _id=login_id)
        is_valid, error_msg = self.validate_input(login)
        if is_valid:
            self.update_existing(login)
            return True, error_msg
        return False, error_msg