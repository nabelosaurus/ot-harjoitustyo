from database_connection import get_database_connection
from entities.user import User
from repositories.user_repository import UserRepository

def register(password, verification):
    if check_password_length(password) and passwords_match(password, verification):
        user = User(_id=None, master_password=password)
        user_repository = UserRepository(get_database_connection())
        success = user_repository.create(user)
        return True if success else False

def passwords_match(password, verification):
    if password == verification:
        return True
    return False


def check_password_length(password):
    if len(password) >= 10:
        return True
    return False


if __name__ == "__main__":
    pass
