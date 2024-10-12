import tkinter as tk
from buttons import set_buttons

def settings(window):
    icon = tk.PhotoImage(file="resources\icn.png")  
    
    window.title('                       🔑Password Manager🔑                           ')
    
    # window.resizable(True,True)
    window.geometry("500x600")
    
    window.iconphoto(False,icon)
    

def f(window):
    
    window.columnconfigure(0,weight = 1)
    window.columnconfigure(1,weight = 1)
    window.columnconfigure(2,weight = 1)
    window.columnconfigure(3,weight = 1)
    window.columnconfigure(4,weight = 1)
    
    window.rowconfigure(0,weight = 1)
    window.rowconfigure(1,weight = 1)
    window.rowconfigure(2,weight = 1)
    window.rowconfigure(3,weight = 1)
    window.rowconfigure(4,weight = 1)
    
    set_buttons(window)
    

def start(window):
    
    window.mainloop()
    