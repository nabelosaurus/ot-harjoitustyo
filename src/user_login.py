from database_connection import get_database_connection
from repositories.user_repository import UserRepository

def login_succesfull(master_password):
    user_repository = UserRepository(get_database_connection())
    password_from_database = user_repository.get_user().master_password
    return bool(master_password == password_from_database)
