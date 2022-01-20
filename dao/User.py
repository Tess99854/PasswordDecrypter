class User:
    def __init__(self, email=None, username=None, password=None) -> None:
        self.email = email
        self.username = username
        self.password = password
        super().__init__()
