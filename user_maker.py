"""Generates a window in order to create a new user"""

#!/usr/bin/python
# user_maker.py
__author__ = "Elijah"
__version__ = 3.7

import tkinter as tk
# from time import sleep

width = 700
height = 500
x_shift = 370
y_shift = 200

username_label       = None
password_label       = None
check_password_label = None
username             = None
password             = None
check_pass           = None
root                 = None


def check(user_name, pass_word):
    """Checks to see if the username and password already exist

    :param user_name: the username created by the user
    :param pass_word: the password created by the user
    :return: True if profile already exists"""

    global username_label, password_label

    file = open("users.txt", "r")
    file_content = file.read()
    words = file_content.split("\n")

    for word in words:
        for i in range(len(word)):
            if word[i] == " ":
                user     = word[0:i]
                new_pass = word[i+1:]

                if user_name == user:
                    if new_pass == pass_word:
                        username_label = tk.Label(root, text="Profile already exists", fg="red")
                        username_label.place(x=275, y=129)
                        return True

    write_file = open("users.txt", "w")
    for i in words:
        write_file.write(str(i) + "\n")

    write_file.write(user_name + " " + pass_word)

    file.close()
    write_file.close()


def enter(event):
    """Gets the username and password and checks to see if they left a box open

    :param event: the event that is detected
    :return: None"""

    global username_label, password_label, check_password_label

    # sleep(0.33)
    user_name = username.get()
    pass_word = password.get()
    check_password = check_pass.get()

    if username_label is not None:
        username_label.destroy()
    if password_label is not None:
        password_label.destroy()
    if check_password_label is not None:
        check_password_label.destroy()

    username.config(highlightbackground="white")
    password.config(highlightbackground="white")
    check_pass.config(highlightbackground="white")

    if len(user_name) == 0:
        username.config(highlightbackground="red")
        username_label = tk.Label(root, text="Unfilled username", fg="red")
        username_label.place(x=450, y=179)

    if len(pass_word) == 0:
        password.config(highlightbackground="red")
        password_label = tk.Label(root, text="Unfilled password", fg="red")
        password_label.place(x=450, y=229)

    if len(check_password) == 0:
        check_pass.config(highlightbackground="red")
        check_password_label = tk.Label(root, text="Unfilled password", fg="red")
        check_password_label.place(x=450, y=279)

    else:
        if pass_word != check_password:
            check_pass.config(highlightbackground="red")
            check_password_label = tk.Label(root, text="Passwords do not match", fg="red")
            check_password_label.place(x=450, y=279)
        else:
            check(user_name, pass_word)


def new_user(event):
    """Creates a new user profile

    :param event: the event that is detected
    :return: None"""

    global username, password, check_pass, root

    root = tk.Tk()
    root.geometry("%dx%d+%d+%d" % (width, height, x_shift, y_shift))
    root.title("New User")

    username   = tk.Entry(root, bd=4, highlightthickness=2)
    password   = tk.Entry(root, bd=4, highlightthickness=2)
    check_pass = tk.Entry(root, bd=4, highlightthickness=2)

    user_label       = tk.Label(root, text="Create your username here:")
    pass_label       = tk.Label(root, text="Create your password here:")
    check_pass_label = tk.Label(root, text="Double check your password:")

    username.place(x=height // 2, y=175)
    password.place(x=height // 2, y=225)
    check_pass.place(x=height // 2, y=275)

    user_label.place(x=70, y=176)
    pass_label.place(x=70, y=227)
    check_pass_label.place(x=60, y=277)

    root.bind('<Return>', enter)
    root.mainloop()
