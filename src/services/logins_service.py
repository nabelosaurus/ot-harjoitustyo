from entities.login import Login
from database_connection import get_database_connection
from repositories.login_repository import LoginRepository
from services.validation_service import validate_input
from services.hashing_service import hashing_service


class LoginService:

    """LoginService handles business logic related of the logins of the application.
    """

    def __init__(self):
        """Constructor for LoginService
        """
        self.login_repository = LoginRepository(get_database_connection())

    def get_all_logins(self):
        """Get and return all the login items.

        Returns:
            list: Returns a list of Login objects (as described in the entities package).
        """
        return self.login_repository.find_all()

    def create_new(self, details):
        """Create a new login entry.

        Args:
            details: A Login object (as described in the entities package), that is being added to the database.
        """
        self.login_repository.create(details)

    def update_existing(self, details):
        """Update existing login item

        Args:
            details: A Login object (as described in the entities package), that is being updated in the database.
        """
        self.login_repository.update_by_id(details)


    def process_save(self, website, username, email, password):
        """Handles validation of inputs, and saving a new login item.

        Args:
            website (str): Website as a string.
            username (str): Username as a string.
            email (str): Email as a string.
            password (str): Password as a string.

        Returns:
            [tuple]: Returns a tuple where the 0-index is a boolean, and the 1-index is a string.
                        0-index: True if input meets validation checks, otherwise False.
                        1-index: Generated error message that is passed to the UI incase of validation fail.
        """
        login = Login(_id=None, website=website, password=password, salt=hashing_service.create_salt(), username=username, email=email)
        is_valid, error_msg = validate_input(login)
        if is_valid:
            self.create_new(login)
            return True, error_msg
        return False, error_msg


    def process_update(self, login_id, website, email, username, password):
        """Handles validation of inputs, and updating an existing login item.

        Args:
            login_id (int): The id of item that is being updated.
            website (str): Website as a string.
            username (str): Username as a string.
            email (str): Email as a string.
            password (str): Password as a string.

        Returns:
            [type]: Returns a tuple where the 0-index is a boolean, and the 1-index is a string.
                        0-index: True if input meets validation checks, otherwise False.
                        1-index: Generated error message that is passed to the UI incase of validation fail.
        """
        login = Login(_id=login_id, website=website, password=password, salt=hashing_service.create_salt(), username=username, email=email)
        is_valid, error_msg = validate_input(login)
        if is_valid:
            self.update_existing(login)
            return True, error_msg
        return False, error_msg