import tkinter as tk
from handlers.handlers import *


def set_buttons(window):
    buttonsignin = tk.Button(
        window,
        text="🎟SIGN IN🎟",
        padx=100,
        pady=10,
        font="garamond-bold",
        command=lambda: signin_handler(buttonsignin, buttonsignup, window),
    )
    buttonsignup = tk.Button(
        window,
        text="🎫SIGN UP🎫",
        padx=50,
        pady=50,
        font="futura-bold",
        command=lambda: signup_handler(buttonsignin, buttonsignup, window),
    )
    buttonsignin.grid(row=4, column=4)
    buttonsignup.grid(column=4, row=3)
