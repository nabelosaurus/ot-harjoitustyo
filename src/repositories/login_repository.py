class Login:
    def __init__(self, _id, website, password, username=None, email=None):
        self.id = _id
        self.website = website
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<{self.id}: {self.website}>"

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
                row["username"], 
                row["email"]) for row in rows]

    def find(self):
        pass

    def create(self, login):
        cursor = self._connection.cursor()
        cursor.execute(
            'insert into logins (website, username, email, password) values (?, ?, ?, ?)',
            (login.website, login.username, login.email, login.password)
        )
        self._connection.commit()
        return True
