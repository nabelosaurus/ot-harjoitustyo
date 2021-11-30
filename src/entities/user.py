class User:
    def __init__(self, _id, master_password):
        self.id = _id
        self.master_password = master_password

    def __repr__(self):
        return f"<{self.id} - {self.master_password}>"
