import tkinter as tk

from dao.User import User
from frames.menu_frame import set_menu_frame
from dao.UserRepository import UserRepository


def set_sign_in_frame(root, user_repository):
    logged : str
    def submit():
        username_text = username.get()
        password_text = password.get()
        if not username_text or not password_text:
            error.config(text='Please fill all the fields')
        else:
            user = User(username_text, password_text)
            try:
                logged = UserRepository.login(username.get(), password.get())
            except Exception as e:
                print(e)
        # Todo: add validation
        # login user
        # logged = UserRepository.login(username.get(), password.get())
        # if logged == 'False':
           # print ("try again")
            
            
    def verificationProcess():
        try :
            verif = UserRepository.loginStepTwo(code.get(), logged)
            goto_menu()
        except Exception as e:
                print(e)


    def goto_menu():
        sign_in_frame.grid_forget()
        root.title('Menu')
        set_menu_frame(root)

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

    error = tk.Label(sign_in_frame, fg='#DB222A', bg='#020426')
    error.grid(row=2)

    buttons_frame = tk.LabelFrame(sign_in_frame, padx=50, pady=10, bg='#020426', borderwidth=0)
    buttons_frame.grid(row=3, columnspan=2)

    space = tk.Label(buttons_frame, text='', bg='#020426', fg='#DB222A', width=25)
    space.grid(row=2, column=1)

    back = tk.Button(buttons_frame, text='<<', bg='#020426', fg='#DB222A')
    back.grid(row=2, column=0)

    submit = tk.Button(buttons_frame, text='Sign in', padx=20, fg='#ebebef', bg='#DB222A', command=submit)
    submit.grid(row=2, column=2)
