import tkinter as tk
from functions.coding import encoding, decoding


def set_encode_decode_frame(root):
    def encode(event):
        encoded = encoding(event.widget.get())
        encoded1.delete(1.0, "end")
        encoded1.insert(1.0, encoded)

    def decode(event):
        decoded = decoding(event.widget.get())
        original2.delete(1.0, "end")
        original2.insert(1.0, decoded)

    encode_decode_frame = tk.LabelFrame(root, padx=50, bg='#020426', borderwidth=0)
    encode_decode_frame.grid(row=1)

    title = tk.Label(encode_decode_frame, text='Encoding and Decoding.', fg='#DB222A', bg='#020426',
                     font=('Raleway', 18), width=35, anchor='w')
    title.grid(row=0, pady=10)

    encode_frame = tk.LabelFrame(encode_decode_frame, text='Encoding', font='Raleway 12 bold', padx=10, fg='#FFF',
                                 bg='#020426', borderwidth=1)
    encode_frame.grid(row=1)

    tk.Label(encode_frame, text="Original message", fg='white', bg='#020426', font=('Raleway', 10), width=20,
             anchor='w').grid(row=0, column=0)
    tk.Label(encode_frame, text="Encoded message", fg='white', bg='#020426', font=('Raleway', 10), width=20,
             anchor='w').grid(row=1, column=0)

    original1 = tk.Entry(encode_frame, width=50, name='1')
    encoded1 = tk.Text(encode_frame, width=37, height=2)

    original1.bind("<Leave>", encode)

    original1.grid(row=0, column=1)
    encoded1.grid(row=1, column=1, pady=10)

    decode_frame = tk.LabelFrame(encode_decode_frame, text='Decoding', font='Raleway 12 bold', padx=10, fg='#FFF',
                                 bg='#020426', borderwidth=1)
    decode_frame.grid(row=2)

    tk.Label(decode_frame, text="Original message", fg='white', bg='#020426', font=('Raleway', 10), width=20,
             anchor='w').grid(row=1, column=0)
    tk.Label(decode_frame, text="Encoded message", fg='white', bg='#020426', font=('Raleway', 10), width=20,
             anchor='w').grid(row=0, column=0)

    encoded2 = tk.Entry(decode_frame, width=50)
    original2 = tk.Text(decode_frame, width=37, height=2)

    encoded2.grid(row=0, column=1)
    original2.grid(row=1, column=1, pady=10)

    encoded2.bind("<Leave>", decode)
