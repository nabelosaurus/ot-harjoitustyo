from entities.user import User
from services.hashing_service import hashing_service


class UserRepository:
    """Repository class for communicating with the users table of the database.
    """

    def __init__(self, connection):
        """Constructor for the UserRepository

        Args:
            connection: sqlite3.connect-object
        """
        self._connection = connection

    def find_all(self):
        """Queries the database for all users, returns a list of User objects.

        Returns:
            [list]: list of User objects
        """
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        return [User(row["id"], row["master_password"]) for row in rows]

    def get_user(self):
        """Get the single registered user of the application.

        Returns:
            User object or False: If users table is empty, returns False. Otherwise will return a single User object (first in database table).
        """
        if self.find_all():
            return self.find_all()[0]
        return False

    def create(self, user):
        """Insert user object into users table.

        Args:
            user: User object that's to be inserted into the database.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into users (master_password) values (?)",
            (hashing_service.encrypt_master(user.master_password),)
        )
        self._connection.commit()
