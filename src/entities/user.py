class User:
    """User object
    """
    def __init__(self, _id, master_password):
        """Constructor of User object

        Args:
            _id (int): id of User object as an integer. Functions as the pk for the db-table as well.
            master_password (str): The master password of the application as a String.
        """
        self.id = _id
        self.master_password = master_password

    def __repr__(self):
        return f"<{self.id} - {self.master_password}>"
