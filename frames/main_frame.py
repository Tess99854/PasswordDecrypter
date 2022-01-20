import tkinter as tk

from frames.sign_in_frame import set_sign_in_frame
from frames.sign_up_frame import set_sign_up_frame


def set_main_frame(root, repository):
    def goto_sign_in():
        main_frame.grid_forget()
        root.title('Sign In')
        set_sign_in_frame(root, repository)

    def goto_sign_up():
        main_frame.grid_forget()
        root.title('Sign Up')
        set_sign_up_frame(root, repository)

    main_frame = tk.LabelFrame(root, padx=50, bg='#020426', borderwidth=0)
    main_frame.grid(row=1)

    title = tk.Label(main_frame, text='Welcome Onboard!', fg='white', bg='#020426', font=('Raleway', 25))
    title.grid(row=0)

    frame = tk.LabelFrame(main_frame, padx=50, bg='#020426', borderwidth=0)
    frame.grid(row=2)

    sign_in_button = tk.Button(frame, text='Sign In', padx=20, bg='#ebebef', fg='#DB222A', command=goto_sign_in)
    space = tk.Label(frame, text='           ', bg='#020426')
    sign_up_button = tk.Button(frame, text='Sign Up', padx=20, bg='#DB222A', fg='#FFF', command=goto_sign_up)

    sign_up_button.grid(row=0, column=0)
    space.grid(row=0, column=1)
    sign_in_button.grid(row=0, column=2)
