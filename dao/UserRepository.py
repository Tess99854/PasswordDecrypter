from datetime import datetime

from dao.User import User
from functions.hashpass import hash_password, verifyPassword
from dao.mailingService import EmailService

  
import random


class UserRepository:
    email_service: EmailService = None

    def __init__(self, connection, email_service) -> None:
        self.conn = connection
        self.cursor = self.conn.cursor()
         self.email_service = email_service
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

    def login(self, username: str, password: str):
        result = self.get(username=username)
        random_number = random.randint(100000, 999999)
        if result is None:
            raise Exception("This user doesn't exists please try another user")
        salt = result.password[32:]
        authpassword = result.password[:32]
        pass_verification = verifyPassword(password, authpassword, salt)
        if pass_verification is True:
            content = f"Code: {random_number}"
            self.email_service.send_email(receiver_email=result.email, content=content)
            return random_number
        else :
            raise Exception("This password is wrong")

    def loginStepTwo (verification_code, generated):
        if verification_code == generated:
                return True
        else :
            raise Exception("This code is wrong")

