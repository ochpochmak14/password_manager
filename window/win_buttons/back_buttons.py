import tkinter as tk

ret = None

def return_button(btn1, btn2, window):
    from handlers.handlers import double_signin_handler
    ret = tk.Button(window, text="Back", fg="blue", command=lambda:double_signin_handler(ret, btn1, btn2, window))
    ret.grid(column=0, row=1)