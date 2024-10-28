import tkinter as tk

from buttons import *

def signin_handler(btn1, btn2, window):
   btn1.after(0, btn1.destroy)
   btn2.after(0, btn2.destroy) 
   
   
    
    
def signup_handler(btn1, btn2, window):
   btn1.after(0, btn1.destroy)
   btn2.after(0, btn2.destroy)

   name_label = tk.Label(window, text='User name')
   name_label.grid(row=3,column=3)
   
   pass_label = tk.Label(window, text='Password')
   pass_label.grid(column=3,row=3,rowspan=2)
   
   secret_code = tk.Label(window, text='Secret code')
   secret_code.grid(column=3, row=4)
   
   user_name = tk.Entry(window, width=50)
   user_name.insert(0, 'Enter user name')
   user_name.grid(column=4, row=3, rowspan=1)

   
   user_password = tk.Entry(window, width=50)
   user_password.insert(0, 'Enter your password')
   user_password.grid(column=4,row=3,rowspan=2)  
   
   secret_code_entry = tk.Entry(window, width=50)
   secret_code_entry.insert(0, 'Enter secret code')
   secret_code_entry.grid(column=4, row=4)
   
   button_sub = tk.Button(window, text='Submit')
   button_sub.grid(row=5, column=4)

   
    