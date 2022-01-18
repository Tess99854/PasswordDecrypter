from dao.User import User


class UserRepository:
    def __init__(self, connection) -> None:
        self.conn = connection
        self.cursor = self.conn.cursor()
        super().__init__()

    def all(self):
        return self.cursor.execute('SELECT * FROM users').fetchall()

    def get(self, pk, email, username):
        query = 'SELECT * FROM users'
        if pk:
            query += ' WHERE id=' + pk
        if email:
            query += ' WHERE email=' + email
        if username:
            query += ' WHERE username=' + username
        return self.cursor.execute(query).fetchOne()

    def add(self, user: User):
        print('added user')

    def update(self, user: User):
        print('added user')
