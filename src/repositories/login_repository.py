from entities.login import Login
from services.hashing_service import hashing_service

class LoginRepository:
    """Repository class for communicating with the logins table of the database.
    """
    def __init__(self, connection):
        """Constructor for the LoginRepository

        Args:
            connection: sqlite3.connect-object
        """
        self._connection = connection

    def find_all(self):
        """Queries the database for all logins, returns a list of Login objects.

        Returns:
            [list]: list of Login objects
        """
        cursor = self._connection.cursor()
        cursor.execute("select * from logins")
        rows = cursor.fetchall()
        return [Login(
                row["id"],
                row["website"],
                row["password"],
                row["salt"],
                row["username"],
                row["email"]) for row in rows]

    def update_by_id(self, login):
        """Update specific row in the logins table by login arguments id.

        Args:
            login: Login object that is being updated.
        """
        token = hashing_service.encrypt_login_password(login)
        cursor = self._connection.cursor()
        cursor.execute(
            "update logins set website = ?, username = ?, email = ?, password = ?, salt = ? WHERE id = ?",
            (login.website, login.username, login.email, token, login.salt, login.id)
        )
        self._connection.commit()
        

    def create(self, login):
        """Insert login object into logins table.

        Args:
            login: Login object that's to be inserted into the database.
        """
        token = hashing_service.encrypt_login_password(login)
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into logins (website, username, email, password, salt) values (?, ?, ?, ?, ?)",
            (login.website, login.username, login.email, token, login.salt)
        )
        self._connection.commit()
