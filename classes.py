"""Checks if the user already has classes. If not, it has the user put them in"""

#!/usr/bin/python
# classes.py
__author__ = "Elijah"
__version__ = 3.7


def check_classes(pos):
    """Checks the classes of the user

    :param pos: the position of the user's classes
    :return: the classes if they are the user's, False if the user has no classes"""

    file = open("classes.txt", "r")
    file_content = file.read()
    words = file_content.split("\n")
    file.close()
    if pos > len(words) - 1 or words[0] == "":
        return False
    else:
        user_classes = words[pos].split(", ")
        return user_classes


def make_classes(classes):
    """Creates new classes for the user

    :param classes: a string that contains all the classes for the user
    :return: None"""

    file = open("classes.txt", "r")
    file_content = file.read()
    words = file_content.split("\n")

    write_file = open("classes.txt", "w")
    if words[0] != "":
        for i in words:
            write_file.write(str(i) + "\n")

    write_file.write(classes)

    file.close()
    write_file.close()
