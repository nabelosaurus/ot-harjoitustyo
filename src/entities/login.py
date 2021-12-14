class Login:
    """Login object
    """

    def __init__(self, _id, website, password, salt=None, username=None, email=None):
        """Constructor of Login object

        Args:
            _id (int or None): Id of Login object as an integer. Functions as the pk for the db-table as well.
            website (str): Website of Login object as a string.
            password (str or bytes): Password of Login object as a string or bytes.
            salt (bytes, optional): Random bytes for salting the password. Defaults to None.
            username (str, optional): Username of Login object as string. Defaults to None.
            email (str, optional): Email of Login object as a string. Defaults to None.
        """
        self.id = _id
        self.website = website
        self.username = username
        self.email = email
        self.password = password
        self.salt = salt

    def __repr__(self):
        return f"<{self.id}: {self.website}>"
