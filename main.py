import tkinter as tk
from window_settings.window_settings import *


def main():
    from db_connect import db_create, db_connect

    my_window = tk.Tk()

    con = db_connect()
    db_create(con)

    settings(my_window)
    f(my_window)
    start(my_window)


if __name__ == "__main__":
    main()
