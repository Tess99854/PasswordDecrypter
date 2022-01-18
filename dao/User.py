class User:
    def __init__(self, email, username, password) -> None:
        self.email = email
        self.username = username
        self.password = password
        super().__init__()

