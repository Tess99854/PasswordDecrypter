from datetime import datetime

from dao.User import User
from functions.hashpass import hash_password


class UserRepository:
    def __init__(self, connection) -> None:
        self.conn = connection
        self.cursor = self.conn.cursor()
        super().__init__()

    def all(self):
        return self.cursor.execute('SELECT * FROM users').fetchall()

    def get(self, pk = None, email=None, username=None):
        query = 'SELECT * FROM users'
        if pk:
            query += ' WHERE id = ' + "'" + pk + "'"
        if email:
            query += ' WHERE email = ' + "'" + email + "'"
        if username:
            query += ' WHERE username = ' + "'" + username + "'"

        self.cursor.execute(query)
        return self.cursor.fetchone()

    def add(self, user: User):
        if self.get(email=user.email) is None:
            insert_user_query = "INSERT INTO users (email, username, password, created_on) VALUES (%s, %s, %s, %s)"
            user.password = hash_password(user.password)
            values = (user.email, user.username, user.password, datetime.now())
            self.cursor.execute(insert_user_query, values)
            self.conn.commit()
        else:
            raise Exception("This user already exists please try another user")

    def update(self, user: User):
        print('added user')
