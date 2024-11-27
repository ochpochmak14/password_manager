import tkinter as tk
from tkinter import ttk
def create_table(window):
    tree = ttk.Treeview(window)
    tree['columns'] = ["ID", "App", "Login", "Password"]
    