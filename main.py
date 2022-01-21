import tkinter as tk
from dao.mailingService import EmailService
from envvars import sender, password

import db
from dao.UserRepository import UserRepository
from frames.main_frame import set_main_frame

if __name__ == '__main__':
    email_service = EmailService(sender_email=sender, sender_password=password)
    root = tk.Tk()
    root.title('Home')

    canvas = tk.Canvas(root, width=1000, height=500, bg='#020426')
    canvas.grid(rowspan=4)

    user_repository = UserRepository(db.connect(), email_service)

    set_main_frame(root, user_repository)

    root.mainloop()
