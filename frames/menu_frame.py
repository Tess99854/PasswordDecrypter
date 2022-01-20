import tkinter as tk

from frames.menu.encoding_frame import set_encode_decode_frame
from frames.menu.hashing_frame import set_hash_attacks_frame


def set_menu_frame(root):
    def goto_encode():
        menu_frame.grid_forget()
        root.title('Encoding & Decoding')
        set_encode_decode_frame(root)

    def goto_hash():
        print('hashing frame')
        menu_frame.grid_forget()
        root.title('Hashing & Attacks')
        set_hash_attacks_frame(root)

    def goto_symmetric_encryption():
        print('goo')

    def goto_asymmetric_encryption():
        print('goo')

    def goto_chat():
        print('goo')

    menu_frame = tk.LabelFrame(root, padx=50, bg='#020426', borderwidth=0)
    menu_frame.grid(row=1)

    title = tk.Label(menu_frame, pady=30, text='Choose your weapon.', fg='#DB222A', bg='#020426', font=('Raleway', 25))
    title.grid(row=0)

    frame = tk.LabelFrame(menu_frame, bg='#020426', borderwidth=0)
    frame.grid(row=2)

    encode_button = tk.Button(frame, text='Encoding', padx=20, bg='#ebebef', fg='#DB222A', command=goto_encode)
    hash_button = tk.Button(frame, text='Hashing', padx=20, bg='#ebebef', fg='#DB222A', command=goto_hash)
    symmetric_encryption_button = tk.Button(frame, wraplength=100, text='Symmetric Encryption', padx=20, bg='#ebebef',
                                            fg='#DB222A', command=goto_symmetric_encryption)
    asymmetric_encryption_button = tk.Button(frame, wraplength=100, text='Asymmetric Encryption', padx=20, bg='#ebebef',
                                             fg='#DB222A', command=goto_asymmetric_encryption)
    chat_button = tk.Button(menu_frame, text='Chat!', padx=20, bg='#DB222A', fg='#FFF', command=goto_chat)

    encode_button.grid(row=0, column=0)
    hash_button.grid(row=0, column=2)
    symmetric_encryption_button.grid(row=1, column=0, pady=20, padx=10)
    asymmetric_encryption_button.grid(row=1, column=2)
    chat_button.grid(row=3, columnspan=2)
