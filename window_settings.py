import tkinter as tk


def settings(window):
    icon = tk.PhotoImage(file="resources\icn.png")

    window.title("                       🔑Password Manager🔑                           ")

    window.geometry("500x600")

    window.iconphoto(False, icon)


def f(window):

    from buttons import set_buttons

    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=1)
    window.columnconfigure(3, weight=1)
    window.columnconfigure(4, weight=1)
    window.columnconfigure(5, weight=1)
    window.columnconfigure(6, weight=1)
    window.columnconfigure(7, weight=1)
    window.columnconfigure(8, weight=1)

    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.rowconfigure(2, weight=1)
    window.rowconfigure(3, weight=1)
    window.rowconfigure(4, weight=1)
    window.rowconfigure(5, weight=1)
    window.rowconfigure(6, weight=1)
    window.rowconfigure(7, weight=1)
    window.rowconfigure(8, weight=1)

    set_buttons(window)


def start(window):

    window.mainloop()
