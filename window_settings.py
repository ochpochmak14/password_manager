import tkinter as tk


def settings(window):
    icon = tk.PhotoImage(file="resources\icn.png")  
    
    window.title('                       🔑Password Manager🔑                           ')
    
    window.resizable(True,True)
    window.geometry("500x600")
    
    window.iconphoto(False,icon)

def start(window):
    
    window.mainloop()
    