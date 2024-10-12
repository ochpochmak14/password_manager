import tkinter as tk

def set_buttons(window):
    buttonsignin = tk.Button(window, text='🎟SIGN IN🎟',padx=100,pady=10, font="garamond-bold")
    buttonsignup = tk.Button(window, text='🎫SIGN UP🎫', padx=50,pady=50, font="futura-bold")
    buttonsignin.grid(row=2, column=2)  
    buttonsignup.grid(column=2, row=1)