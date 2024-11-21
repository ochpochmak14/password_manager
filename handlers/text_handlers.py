import tkinter as tk


def signin_text_handler(e1, e2, btn1, btn2, lb1, lb2, lb3, window):
    from db_operations.db_connect import db_connect

    usn = str(e1.get())
    usp = str(e2.get())
    try:
        connection = db_connect()
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(f"""SELECT * FROM users WHERE user_name = %s""", (usn,))
        table_data = cursor.fetchall()
        if usp == table_data[0][2]:
            print("okkkkkk")
    except Exception as er:
        print(er)
        if connection:
            cursor.close()
            connection.close()


def signup_text_handling(e1, e2, e3, btn1, btn2, lb1, lb2, lb3, window):
    from db_operations.db_connect import db_connect
    from handlers.handlers import main_menu

    global warn
    usn = str(e1.get())
    usp = str(e2.get())
    scs = str(e3.get())
    is_ok = True

    try:
        if usn != "" and usp != "" and scs != "":
            connection = db_connect()
            sql1 = """INSERT INTO users (user_name, user_password, user_secretcode) VALUES (%s, %s, %s)"""
            dt = (usn, usp, scs)
            with connection.cursor() as cursor:
                cursor.execute(sql1, dt)

            connection.commit()
            main_menu(e1, e2, e3, btn1, btn2, lb1, lb2, lb3, window)
        else:
            is_ok = False

            warn = tk.Label(
                window, text="CHECK YOUR USER NAME AND PASSWORD AGAIN", fg="red"
            )
            warn.grid(row=1, column=4)
    except Exception as er:

        is_ok = False

        print(er)

        warn = tk.Label(
            window, text="CHECK YOUR USER NAME AND PASSWORD AGAIN", fg="red"
        )
        warn.grid(row=1, column=4)
        warn.after(2000, warn.destroy)

    if is_ok:

        success = tk.Label(window, text="NOW YOU CAN SIGN IN!", fg="green")
        success.grid(row=1, column=4)
