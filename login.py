"""Creates a login window for the user to login. The user can also create a new profile if they don't have
one already made. Then, if they are logging in, the program will display all the user's classes
depending on the current day."""

#!/usr/bin/python
# login.py
__author__ = "Elijah"
__version__ = 3.7

import tkinter as tk
# from time import sleep
from user_maker import new_user

login = tk.Tk()

width = 700
height = 500
x_shift = 370
y_shift = 200

login.title("Login")
login.geometry("%dx%d+%d+%d" % (width, height, x_shift, y_shift))

username_entry = tk.Entry(login, bd=4)
password_entry = tk.Entry(login, bd=4)

username_entry.place(x=height // 2, y=200)
password_entry.place(x=height // 2, y=250)

# makes the password '****'
password_entry.config(show="*")

user_label = tk.Label(login, text="Username:")
pass_label = tk.Label(login, text="Password:")
text = tk.Text(login, height=1, width=8, font="Arial 12", highlightthickness=0)

username_label   = None
password_label   = None
wrong_user       = None
wrong_pass       = None
hide_pass_label  = None
show_pass_label  = None

user_label.place(x=174, y=203)
pass_label.place(x=175, y=253)
text.place(x=300, y=300)

hide_pass_img = tk.PhotoImage(file="hide_pass.png")
show_pass_img = tk.PhotoImage(file="show_pass.png")


def enter(event):
    """Gets the login username and password from the user and checks to see if they left a box open

    :param event: the event that is detected
    :return: True if the user is a guest"""

    global username_label, password_label

    # sleep(0.33)

    username = username_entry.get()
    password = password_entry.get()

    if username_label is not None:
        username_label.destroy()

    if password_label is not None:
        password_label.destroy()

    if username.lower() == "guest":
        import class_maker
        login.destroy()
        class_maker.main("guest")
        return True

    if len(username) == 0:
        username_label = tk.Label(login, text="Please enter your username", fg="red")
        username_label.place(x=450, y=203)
    if len(password) == 0:
        password_label = tk.Label(login, text="Please enter your password", fg="red")
        password_label.place(x=450, y=253)
    else:
        check(username, password)


def set_incorrect(username=None, password=None):
    """Takes in the username and password and tells the user if they are incorrect or not

    :param username: the incorrect username, otherwise None
    :param password: the incorrect password, otherwise None
    :return: None"""

    global wrong_user, wrong_pass

    if wrong_user is not None:
        wrong_user.destroy()
    if wrong_pass is not None:
        wrong_pass.destroy()

    username_entry.config(highlightbackground="white", highlightthickness=2)
    password_entry.config(highlightbackground="white", highlightthickness=2)

    if username is not None:
        username_entry.config(highlightbackground="red", highlightthickness=2)
        wrong_user = tk.Label(login, text="Incorrect username", fg="red")
        wrong_user.place(x=450, y=203)

    if password is not None:
        password_entry.config(highlightbackground="red", highlightthickness=2)
        wrong_pass = tk.Label(login, text="Incorrect password", fg="red")
        wrong_pass.place(x=450, y=253)


def check(username, password):
    """Checks the users file to see if the user has an account

    :param username: the username sent by the user
    :param password: the password sent by the user
    :return: True if the username and password match"""

    file = open("users.txt", "r")
    file_content = file.read()
    words = file_content.split("\n")
    file.close()

    for count, word in enumerate(words):
        for i in range(len(word)):
            if word[i] == " ":
                user      = word[0:i]
                pass_word = word[i + 1:]

                if username == user:
                    if pass_word == password:
                        login.destroy()
                        import classes, class_maker
                        choice = classes.check_classes(count)
                        if not choice:
                            class_maker.main()
                        else:
                            class_maker.submit(choice)
                        quit()
                    else:
                        set_incorrect(password=password)

                elif pass_word == password:
                    set_incorrect(username=username)
                else:
                    set_incorrect(username, password)


def mouse_enter(event):
    """Detects when the mouse hovers over the text

    :param event: the event that is detected
    :return: None"""

    text.config(font="Arial 12 underline")


def mouse_exit(event):
    """Detects when the mouse stops hovering over the text

    :param event: the event that is detected
    :return: None"""

    text.config(font="Arial 12")


def show_pass(event):
    """Shows the password

    :param event: the event that is detected
    :return: None"""

    hide_pass_label.place_forget()
    show_pass_label.place(x=150, y=253)
    password_entry.config(show="")


def hide_pass(event):
    """Hides the password

    :param event: the event that is detected
    :return: None"""

    show_pass_label.place_forget()
    hide_pass_label.place(x=150, y=253)
    password_entry.config(show="*")


def main():
    """Runs the main program

    :return: None"""

    global show_pass_label, hide_pass_label

    hide_pass_label = tk.Label(login, image=hide_pass_img)
    show_pass_label = tk.Label(login, image=show_pass_img)

    hide_pass_label.place(x=150, y=253)

    text.tag_config("tag", foreground="blue")
    text.tag_bind("tag", "<Button-1>", new_user)
    text.insert('end', "New User", "tag")

    text.bind("<Enter>", mouse_enter)
    text.bind("<Leave>", mouse_exit)

    hide_pass_label.bind("<Button-1>", show_pass)
    show_pass_label.bind("<Button-1>", hide_pass)

    login.bind('<Return>', enter)  # listens for the enter key
    login.mainloop()


if __name__ == '__main__':
    main()
