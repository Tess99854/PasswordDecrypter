import tkinter as tk

from frames.main_frame import set_main_frame
from frames.sign_up_frame import set_sign_up_frame

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Home')

    canvas = tk.Canvas(root, width=600, height=300, bg='#020426')
    canvas.grid(rowspan=4)

    set_main_frame(root)
    # set_sign_up_frame(root)
    root.mainloop()
