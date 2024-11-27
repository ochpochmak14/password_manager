import tkinter as tk
def delete(e1, e2, btn1, btn2, lb1, lb2, lb3, window):
    btn1.after(0, btn1.destroy)
    btn2.after(0, btn2.destroy)
    e1.after(0, e1.destroy)
    e2.after(0, e2.destroy)
    lb1.after(0, lb1.destroy)
    lb2.after(0, lb2.destroy)