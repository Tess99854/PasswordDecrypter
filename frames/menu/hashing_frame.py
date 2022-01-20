import tkinter as tk
from functions.hashing import hashing
from functions.attacks import attacks


def set_hash_attacks_frame(root):
    def hash_text(event):
        algorithm = variable.get()
        text = event.widget.get()
        if text != '':
            hashed = hashing(text, algorithm)
            hashed1.delete(1.0, "end")
            hashed1.insert(1.0, hashed)

    def attack(event):
        algorithm = variable.get()
        text = event.widget.get()
        if text != '':
            attack_attempt = attacks(event.widget.get(), algorithm)
            result.config(text=attack_attempt)

    hash_attacks_frame = tk.LabelFrame(root, bg='#020426', borderwidth=0)
    hash_attacks_frame.grid(row=1)

    options = [
        "MD5",
        "SHA1",
        "SHA256"
    ]

    title = tk.Label(hash_attacks_frame, text='Hashing and attacks.', fg='#DB222A', bg='#020426',
                     font=('Raleway', 18), width=35, anchor='w')
    title.grid(row=0, column=0, pady=10)

    variable = tk.StringVar(hash_attacks_frame)
    variable.set(options[0])

    drop_down = tk.OptionMenu(hash_attacks_frame, variable, *options)
    drop_down.grid(row=0, column=1)

    hash_frame = tk.LabelFrame(hash_attacks_frame, text='Hashing', font='Raleway 12 bold', padx=10, fg='#FFF',
                               bg='#020426', borderwidth=1)
    hash_frame.grid(row=1)

    tk.Label(hash_frame, text="Original message", fg='white', bg='#020426', font=('Raleway', 10), width=20,
             anchor='w').grid(row=0, column=0)
    tk.Label(hash_frame, text="Hashed message", fg='white', bg='#020426', font=('Raleway', 10), width=20,
             anchor='w').grid(row=1, column=0)

    original1 = tk.Entry(hash_frame, width=50)
    hashed1 = tk.Text(hash_frame, width=37, height=2)

    original1.bind("<Leave>", hash_text)

    original1.grid(row=0, column=1)
    hashed1.grid(row=1, column=1, pady=10)

    attack_frame = tk.LabelFrame(hash_attacks_frame, text='Attack', font='Raleway 12 bold', padx=10, fg='#FFF',
                                 bg='#020426', borderwidth=1)
    attack_frame.grid(row=2)

    tk.Label(attack_frame, text="Original message", fg='white', bg='#020426', font=('Raleway', 10), width=20,
             anchor='w').grid(row=0, column=0)
    result = tk.Label(attack_frame, text='enter something to test', fg='white', bg='#020426', font=('Raleway', 10),
                      width=20, anchor='w')

    hashed2 = tk.Entry(attack_frame, width=50)

    hashed2.grid(row=0, column=1)
    hashed2.bind("<Leave>", attack)

    result.grid(row=1)
