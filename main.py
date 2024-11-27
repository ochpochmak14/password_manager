import tkinter as tk
from window_settings.window_settings import *


def main():
    from db_operations.db_connect import db_connect
    from db_operations.create_db import db_create
    
    my_window = tk.Tk()

    con = db_connect()
    db_create(con)
    
    settings(my_window)
    f(my_window)
    start(my_window)


if __name__ == "__main__":
    main()
