from entities.login import Login
from services.hashing_service import hashing_service

class LoginRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
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

    def create(self, login):
        token = hashing_service.encrypt_login_password(login)
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into logins (website, username, email, password, salt) values (?, ?, ?, ?, ?)",
            (login.website, login.username, login.email, token, login.salt)
        )
        self._connection.commit()
        return True
