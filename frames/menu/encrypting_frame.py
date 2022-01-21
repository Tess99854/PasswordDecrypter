import tkinter as tk
#from function.symetricEncryption import encrypt, decrypt

def set_encrypt_decrypt_frame(root, encryption_type):
    if encryption_type == 'symmetric':
        from functions.symetricEncryption import encrypt, decrypt
        options = ["DES", "AES"]
    elif encryption_type == 'asymmetric':
        from functions.asymetricEncryption import encrypt, decrypt
        options = ["RSA", "elGamal"]

    def encrypt_text(event):
        algorithm = variable.get()
        text = event.widget.get()
        if text != '':
            encrypted = encrypt(text, algorithm)
            encrypted1.delete(1.0, "end")
            encrypted1.insert(1.0, encrypted)

    def decrypt_text(event):
        algorithm = variable.get()
        text = event.widget.get()
        if text != '':
            decrypted = decrypt(text, algorithm)
            original2.delete(1.0, "end")
            original2.insert(1.0, decrypted)

    encrypt_decrypt_frame = tk.LabelFrame(root, bg='#020426', borderwidth=0)
    encrypt_decrypt_frame.grid(row=1)

    title = tk.Label(encrypt_decrypt_frame, text='Encryption & Decryption.', fg='#DB222A', bg='#020426',
                     font=('Raleway', 18), width=35, anchor='w')
    title.grid(row=0, column=0, pady=10)

    variable = tk.StringVar(encrypt_decrypt_frame)
    variable.set(options[0])

    drop_down = tk.OptionMenu(encrypt_decrypt_frame, variable, *options)
    drop_down.grid(row=0, column=1)

    encrypt_frame = tk.LabelFrame(encrypt_decrypt_frame, text='Encrypting', font='Raleway 12 bold', padx=10,
                                  fg='#FFF', bg='#020426', borderwidth=1)
    encrypt_frame.grid(row=1)

    tk.Label(encrypt_frame, text="Original message", fg='white', bg='#020426', font=('Raleway', 10), width=20,
             anchor='w').grid(row=0, column=0)
    tk.Label(encrypt_frame, text="Encrypted message", fg='white', bg='#020426', font=('Raleway', 10), width=20,
             anchor='w').grid(row=1, column=0)

    original1 = tk.Entry(encrypt_frame, width=50)
    encrypted1 = tk.Text(encrypt_frame, width=37, height=2)

    original1.bind("<Leave>", encrypt_text)

    original1.grid(row=0, column=1)
    encrypted1.grid(row=1, column=1, pady=10)

    decrypt_frame = tk.LabelFrame(encrypt_decrypt_frame, text='Decrypting', font='Raleway 12 bold', padx=10,
                                  fg='#FFF',
                                  bg='#020426', borderwidth=1)
    decrypt_frame.grid(row=2)

    tk.Label(decrypt_frame, text="Original message", fg='white', bg='#020426', font=('Raleway', 10), width=20,
             anchor='w').grid(row=1, column=0)
    tk.Label(decrypt_frame, text="Encrypted message", fg='white', bg='#020426', font=('Raleway', 10), width=20,
             anchor='w').grid(row=0, column=0)

    decrypted2 = tk.Entry(decrypt_frame, width=50)
    original2 = tk.Text(decrypt_frame, width=37, height=2)

    decrypted2.grid(row=0, column=1)
    original2.grid(row=1, column=1, pady=10)

    decrypted2.bind("<Leave>", decrypt_text)

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Symmetric Encryption & Decryption')
    set_encrypt_decrypt_frame(root, encryption_type='symmetric')
