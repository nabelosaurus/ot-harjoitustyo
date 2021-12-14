from entities.user import User
from database_connection import get_database_connection
from repositories.user_repository import UserRepository
from services.hashing_service import hashing_service


class UserService:

    def __init__(self):
        self.user_repository = UserRepository(get_database_connection())

    def is_registered(self):
        return bool(self.user_repository.get_user())

    def register(self, password, verification):
        if self.check_password_length(password) and self.passwords_match(password, verification):
            user = User(_id=None, master_password=password)
            self.user_repository.create(user)
            return True
        return False

    def passwords_match(self, password, verification):
        if password == verification:
            return True
        return False

    def check_password_length(self, password):
        if len(password) >= 10:
            return True
        return False

    def login_succesfull(self, master_password):
        password_from_database = self.user_repository.get_user().master_password
        return hashing_service.verify_master(password_from_database, master_password)
