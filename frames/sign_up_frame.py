import tkinter as tk
from dao.User import User


def set_sign_up_frame(root, user_repository):
    def submit():
        username_text = username.get()
        password_text = password.get()
        email_text = email.get()
        if not username_text or not password_text or not email_text:
            error.config(text='Please fill all the fields')
        else:
            user = User(email_text, username_text, password_text)
            try:
                user_repository.add(user)
                error.config(text='')
                print('user submitted successfully')
            except Exception as e:
                error.config(text=str(e))


    sign_up_frame = tk.LabelFrame(root, padx=100, bg='#020426', borderwidth=1)
    sign_up_frame.grid(row=1)

    title = tk.Label(sign_up_frame, text='Sign Up.', fg='#DB222A', bg='#020426', font=('Raleway', 25), pady=20)
    title.grid(row=0)

    frame = tk.LabelFrame(sign_up_frame, padx=50, bg='#020426', borderwidth=0)
    frame.grid(row=1, columnspan=2)

    tk.Label(frame, text="Email", fg='white', bg='#020426', font=('Raleway', 10), width=10, anchor='w').grid(row=0)
    tk.Label(frame, text="Username", fg='white', bg='#020426', font=('Raleway', 10), width=10, anchor='w').grid(row=1)
    tk.Label(frame, text="Password", fg='white', bg='#020426', font=('Raleway', 10), width=10, anchor='w').grid(row=2)

    username = tk.Entry(frame)
    password = tk.Entry(frame, show='*')
    email = tk.Entry(frame)

    email.grid(row=0, column=1)
    username.grid(row=1, column=1)
    password.grid(row=2, column=1)

    error = tk.Label(sign_up_frame, fg='#DB222A', bg='#020426')
    error.grid(row=2)

    buttons_frame = tk.LabelFrame(sign_up_frame, padx=50, pady=10, bg='#020426', borderwidth=0)
    buttons_frame.grid(row=3, columnspan=2)

    space = tk.Label(buttons_frame, text='', bg='#020426', fg='#DB222A', width=25)
    space.grid(row=2, column=1)

    back = tk.Button(buttons_frame, text='<<', bg='#020426', fg='#DB222A')
    back.grid(row=2, column=0)

    submit = tk.Button(buttons_frame, text='Submit', padx=20, fg='#ebebef', bg='#DB222A', command=submit)
    submit.grid(row=2, column=2)
