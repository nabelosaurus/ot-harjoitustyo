class Login:
    def __init__(self, _id, website, password, salt=None, username=None, email=None):
        self.id = _id
        self.website = website
        self.username = username
        self.email = email
        self.password = password
        self.salt = salt

    def __repr__(self):
        return f"<{self.id}: {self.website}>"
