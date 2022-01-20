import tkinter as tk

from dao.User import User
from frames.menu_frame import set_menu_frame


def set_sign_in_frame(root, user_repository):
    def submit():
        # Todo: add validation
        user = User(username.get(), password.get())
        # login user
        goto_menu()

    def goto_menu():
        sign_in_frame.grid_forget()
        root.title('Menu')
        set_menu_frame(root)
        print('going to menu..')

    sign_in_frame = tk.LabelFrame(root, padx=100, bg='#020426', borderwidth=1)
    sign_in_frame.grid(row=1)

    title = tk.Label(sign_in_frame, text='Sign In.', fg='#DB222A', bg='#020426', font=('Raleway', 25), pady=20)
    title.grid(row=0)

    frame = tk.LabelFrame(sign_in_frame, padx=50, bg='#020426', borderwidth=0)
    frame.grid(row=1, columnspan=2)

    tk.Label(frame, text="Username", fg='white', bg='#020426', font=('Raleway', 10), width=10, anchor='w').grid(row=0)
    tk.Label(frame, text="Password", fg='white', bg='#020426', font=('Raleway', 10), width=10, anchor='w').grid(row=1)

    username = tk.Entry(frame)
    password = tk.Entry(frame, show='*')

    username.grid(row=0, column=1)
    password.grid(row=1, column=1)

    buttons_frame = tk.LabelFrame(sign_in_frame, padx=50, pady=10, bg='#020426', borderwidth=0)
    buttons_frame.grid(row=2, columnspan=2)

    space = tk.Label(buttons_frame, text='', bg='#020426', fg='#DB222A', width=25)
    space.grid(row=2, column=1)

    back = tk.Button(buttons_frame, text='<<', bg='#020426', fg='#DB222A')
    back.grid(row=2, column=0)

    submit = tk.Button(buttons_frame, text='Sign in', padx=20, fg='#ebebef', bg='#DB222A', command=submit)
    submit.grid(row=2, column=2)
