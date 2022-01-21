import tkinter as tk

import db
from dao.UserRepository import UserRepository
from frames.main_frame import set_main_frame

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Home')

    canvas = tk.Canvas(root, width=600, height=300, bg='#020426')
    canvas.grid(rowspan=4)

    # connection = db.connect()
    user_repository = UserRepository(db.connect())

    set_main_frame(root, user_repository)

    root.mainloop()
