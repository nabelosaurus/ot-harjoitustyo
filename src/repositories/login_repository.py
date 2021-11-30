from database_connection import get_database_connection

class Login:
    def __init__(self, id, website, password, username=None, email=None):
        self.id = id
        self.website = website
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<{self.website}: {self.username}/{self.email}>"

class LoginRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from logins")
        rows = cursor.fetchall()
        return [Login(row["id"], row["website"], row["password"], row["username"], row["email"]) for row in rows]

    def find(self):
        pass

    def create(self):
        pass
