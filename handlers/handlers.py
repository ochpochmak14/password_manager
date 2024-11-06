import tkinter as tk


def main_menu(e1, e2, e3, btn1, btn2, lb1, lb2, lb3, window):

    from buttons import set_buttons

    e1.after(0, e1.destroy)
    e2.after(0, e2.destroy)
    e3.after(0, e3.destroy)
    btn1.after(0, btn1.destroy)
    btn2.after(0, btn2.destroy)
    lb1.after(0, lb1.destroy)
    lb2.after(0, lb2.destroy)
    lb3.after(0, lb3.destroy)

    set_buttons(window)


def signin_handler(btn1, btn2, window):
    from handlers.text_handlers import signin_text_handler, signup_text_handling

    btn1.after(0, btn1.destroy)
    btn2.after(0, btn2.destroy)
    name_label = tk.Label(window, text="User name")
    name_label.grid(row=2, column=3)

    pass_label = tk.Label(window, text="Password")
    pass_label.grid(column=3, row=2, rowspan=2)

    secret_code = tk.Label(window, text="Secret code")

    user_name = tk.Entry(window, width=50)
    user_name.insert(0, "Enter user name")
    user_name.grid(column=4, row=2, rowspan=1)

    user_password = tk.Entry(window, width=50)
    user_password.insert(0, "Enter your password")
    user_password.grid(column=4, row=2, rowspan=2)

    secret_code_entry = tk.Entry(window, width=50)
    secret_code_entry.insert(0, "Enter secret code")

    button_sub = tk.Button(
        window,
        text="Submit",
        command=lambda: signin_text_handler(
            user_name,
            user_password,
            back_button,
            button_sub,
            name_label,
            pass_label,
            secret_code,
            window,
        ),
    )
    button_sub.grid(row=3, column=4)

    back_button = tk.Button(
        window,
        text="Back",
        fg="blue",
        command=lambda: main_menu(
            user_name,
            secret_code_entry,
            user_password,
            button_sub,
            back_button,
            name_label,
            pass_label,
            secret_code,
            window,
        ),
    )
    back_button.grid(column=1, row=1)


def signup_handler(btn1, btn2, window):
    from handlers.text_handlers import signup_text_handling

    btn1.after(0, btn1.destroy)
    btn2.after(0, btn2.destroy)

    name_label = tk.Label(window, text="User name")
    name_label.grid(row=3, column=3)

    pass_label = tk.Label(window, text="Password")
    pass_label.grid(column=3, row=3, rowspan=2)

    secret_code = tk.Label(window, text="Secret code")
    secret_code.grid(column=3, row=4)

    user_name = tk.Entry(window, width=50)
    user_name.insert(0, "Enter user name")
    user_name.grid(column=4, row=3, rowspan=1)

    user_password = tk.Entry(window, width=50)
    user_password.insert(0, "Enter your password")
    user_password.grid(column=4, row=3, rowspan=2)

    secret_code_entry = tk.Entry(window, width=50)
    secret_code_entry.insert(0, "Enter secret code")
    secret_code_entry.grid(column=4, row=4)

    button_sub = tk.Button(
        window,
        text="Submit",
        command=lambda: signup_text_handling(
            user_name,
            user_password,
            secret_code_entry,
            back_button,
            button_sub,
            name_label,
            pass_label,
            secret_code,
            window,
        ),
    )
    button_sub.grid(row=5, column=4)

    back_button = tk.Button(
        window,
        text="Back",
        fg="blue",
        command=lambda: main_menu(
            user_name,
            secret_code_entry,
            user_password,
            button_sub,
            back_button,
            name_label,
            pass_label,
            secret_code,
            window,
        ),
    )
    back_button.grid(column=1, row=1)

