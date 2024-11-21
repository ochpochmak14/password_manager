def password_table_creating(window):
    from tkinter import ttk
    import tkinter as tk
    tree = ttk.Treeview(columns=("id", "app", "login", "password"), show="headings")
    tree.heading("id",text="ID")
    tree.heading("app", text="App")
    tree.heading("login", text="Login")
    tree.heading("password", text="Password")
        
