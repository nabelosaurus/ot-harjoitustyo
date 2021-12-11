from entities.user import User
from services.hashing_service import encrypt_master

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        return [User(row["id"], row["master_password"]) for row in rows]

    def get_user(self):
        if self.find_all():
            return self.find_all()[0]
        return False

    def create(self, user):
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into users (master_password) values (?)", (encrypt_master(user.master_password),)
        )
        self._connection.commit()
        return True
