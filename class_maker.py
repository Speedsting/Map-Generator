"""Takes in classes from the user and shows which classes they have at which times today"""

# !/usr/bin/python
# class_maker.py
__author__ = "Elijah"
__version__ = 3.7

import tkinter as tk
import datetime
import time

current_date = datetime.datetime.now()
day = current_date.weekday()

advisory = False
if day == 2:
    advisory = True

guest = None
final_list = []

root = tk.Tk()

width = 700
height = 500
x_shift = 20
y_shift = 0

colors = ["red", "orange", "green", "blue", "purple", "black", "brown", "pink"]

msg = "Please enter all your classes for your schedule (just enter 'lunch' for lunch, " \
      "'111' for gym, and '0' for free blocks)."

label_msg = tk.Label(root, text=msg)

root.title("CCHS Map GPS")
root.geometry("%dx%d+%d+%d" % (width, height, x_shift, y_shift))

block_a = tk.Entry(root, bd=3)
block_b = tk.Entry(root, bd=3)
block_c = tk.Entry(root, bd=3)
block_d = tk.Entry(root, bd=3)
block_e = tk.Entry(root, bd=3)
block_f = tk.Entry(root, bd=3)
block_g = tk.Entry(root, bd=3)
block_h = tk.Entry(root, bd=3)

choices = [block_a, block_b, block_c, block_d, block_e, block_f, block_g, block_h]

label_a = tk.Label(root, text="A")
label_b = tk.Label(root, text="B")
label_c = tk.Label(root, text="C")
label_d = tk.Label(root, text="D")
label_e = tk.Label(root, text="E")
label_f = tk.Label(root, text="F")
label_g = tk.Label(root, text="G")
label_h = tk.Label(root, text="H")

labels = [label_a, label_b, label_c, label_d, label_e, label_f, label_g, label_h]
student_classes = []

for num, label in enumerate(labels):
    label.grid(row=num, column=0)

for num, block in enumerate(choices):
    block.grid(row=num, column=1)

label_msg.place(x=0, y=height-25)

debug = False


def submit(class_rooms=None):
    """Gets the values of each entry box

    :param class_rooms: the classes of the user if the user has made classes before
    :return: None"""

    global guest

    if class_rooms is None:
        a, b, c, d, e, f, g, h = choices
        class_a = a.get()
        class_b = b.get()
        class_c = c.get()
        class_d = d.get()
        class_e = e.get()
        class_f = f.get()
        class_g = g.get()
        class_h = h.get()

        classrooms = class_a + ", " + class_b + ", " + class_c + ", " + class_d + ", " + class_e
        classrooms += ", " + class_f + ", " + class_g + ", " + class_h
        
        if guest is None:
            import classes
            classes.make_classes(classrooms)

    else:
        root.withdraw()
        class_a, class_b, class_c, class_d, class_e, class_f, class_g, class_h = class_rooms

    blocks = [class_a, class_b, class_c, class_d, class_e, class_f, class_g, class_h]
    make_blocks(blocks)


def make_blocks(classes):
    """Determines which class the user has for each block they entered in

    :param classes: the classes entered in by the user
    :return: None"""

    global student_classes

    biology_classes       = [435, 436, 440, 441]
    earth_science_classes = [401, 449]
    chemistry_classes     = [404, 408, 445, 446]
    physics_classes       = [429, 431]
    math_classes          = [412, 415, 418, 419, 420, 423, 438, 443]
    social_studies        = [314, 316, 318, 339, 340, 341, 343, 346]
    world_language        = [301, 305, 309, 348, 349, 350, 351]
    english_classes       = [322, 325, 326, 327, 328, 329, 330, 332, 333, 334, 335]
    elective_classes      = [138, 140, 141, 248, 253, 254, 256, 257, 261, 424, 426, 427]
    gym_classes           = [104, 105, 111, 121, 122]
    coding                = [411]

    student_schedule = {}
    student_classes  = []

    class_names = ["Biology", "Planet Earth", "Chemistry", "Physics", "Math", "Social Studies", "Language",
                   "English", "Elective", "Gym", "Coding"]

    class_types = [biology_classes, earth_science_classes, chemistry_classes, physics_classes, math_classes,
                   social_studies, world_language, english_classes, elective_classes, gym_classes, coding]

    blocks = ["A", "B", "C", "D", "E", "F", "G", "H"]

    change = False
    lunch  = False

    if not advisory:
        times = [" 8:00  -  9:00", " 9:04  - 10:04", "10:08 - 11:08", "11:12 - 11:59",
                 "12:02 - 12:49", "12:52 -  1:39", " 1:43  -  2:41"]
    else:
        times = ["8:00   -  8:56", "9:00   -  9:56", "9:59   - 10:22", "10:25 - 11:20",
                 "11:24 - 12:08", "12:11 - 12:55", "12:58 -  1:42", "1:46  -  2:41"]

    for counter, room in enumerate(classes):
        for i, classroom in enumerate(class_types):
            for class_num in classroom:
                if advisory and counter == 2 and not change:
                    change = True
                    student_classes.append("Advisory")
                    student_schedule["Advisory"] = "Advisory"
                try:
                    if int(room) == class_num:
                        student_schedule[blocks[counter]] = class_names[i]
                        student_classes.append(room)
                    elif int(room) == 0:
                        student_schedule[blocks[counter]] = "Study"
                        student_classes.append('Study')

                except ValueError:
                    if str(room).lower() == "lunch" and not lunch:
                        lunch = True
                        student_schedule[blocks[counter]] = "Lunch"
                        student_classes.append("Lunch")

    create_times(student_schedule, student_classes, times)


def create_times(schedule, classes, times):
    """Figures out which class is cancelled depending on the day and prints out the schedule with times

    :param schedule: a dictionary that contains the user's schedule
    :param classes: a list that contains the user's classroom numbers
    :param times: a list that contains all the class start and end times
    :return: None"""

    global final_list

    # checks which class is being skipped
    g_block = 2
    skip    = 0
    switch       = False
    other_switch = False

    final_list = []

    if advisory:
        place = 7
    else:
        place = 6

    if day == 0:
        skip    = 10
        g_block = 10
    elif day == 1:
        skip    = 2
    elif day == 2:
        skip    = 8
        g_block = 8
    elif day == 3:
        skip    = 1
    elif day == 4:
        skip    = 0

    if not debug:
        for counter, i in enumerate(schedule.items()):
            if switch and not other_switch and not advisory:
                counter -= 1
            elif other_switch and not switch and not advisory:
                counter += 1
    
            if "G" in i:
                switch = True
            elif counter < skip:
                if classes[counter] != "Advisory" and skip != 0:
                    string = times[counter], classes[counter], i
                    final_list.append(string)
                elif skip == 0:
                    string = times[counter], classes[counter], i
                    final_list.append(string)
                else:
                    string = times[counter], classes[counter]
                    final_list.append(string)
    
            elif counter > skip:
                if skip != 0 and skip != 1:
                    string = times[counter], classes[counter], i
                    final_list.append(string)
                else:
                    string = times[counter - 1], classes[counter], i
                    final_list.append(string)
            
            if counter < skip and counter == g_block:
                if skip == 0 or skip == 1:
                    other_switch = True
                value = str(schedule.values())
                key = str(schedule.keys())

                place1 = key.find("G")
                pos1 = key.find("'", place1)
                place2 = value.find(schedule["G"])
                pos2 = value.find("'", place2)
   
                key = key[place1:pos1]
                value = value[place2:pos2]

                string = times[counter], classes[place], key, value
                final_list.append(string)
            
            elif counter >= skip and counter == g_block:
                if skip == 0 or skip == 1:
                    other_switch = True
                value = str(schedule.values())
                key = str(schedule.keys())
   
                place1 = key.find("G")
                pos1 = key.find("'", place1)
                place2 = value.find(schedule["G"])
                pos2 = value.find("'", place2)
   
                key = key[place1:pos1]
                value = value[place2:pos2]
   
                if advisory:
                    string = times[counter - 1], classes[place], key, value
                    final_list.append(string)
                else:
                    string = times[counter], classes[place], key, value
                    final_list.append(string)

        app = tk.Tk()
        map_btn = tk.Button(app, text="Generate Map", command=generate_map)
        map_btn.place(x=500, y=100)
        app.geometry("%dx%d+%d+%d" % (width, height, 0, 0))
        app.title("Classes")

        space = 0

        for count, i in enumerate(final_list):
            string = str(i)
            print(i)
            string = string.replace("(", "")
            string = string.replace(")", "")
            string = string.replace("'", "")

            if space == 0:
                place = len(string)
                string = string.replace(",", "\t")
                space = len(string) - place
            else:
                space_string = ""
                for j in range(space):
                    space_string += " "
                string = string.replace(",", space_string)

            thing = tk.Label(app, text=string, font="Verana 15")
            thing.grid(row=count, column=0, sticky="W")

        root.destroy()
        app.mainloop()

def generate_map():
    """Calls the mapmaker to make a map of the school based on the user's classes"""

    global student_classes
    import map

    for count, classroom in enumerate(final_list):
        classroom = classroom[1]
        if classroom == 0 or classroom == "Lunch":
            classroom = "112"
        if count != 0:
            other_class = student_classes[count - 1]
            room1 = "room" + classroom
            room2 = "room" + other_class
            if str(classroom)[0: 1] != str(other_class)[0: 1]:
                print("Making stairs")
                # time.sleep(5)
                stair = map.draw_lines(room1, room2, color=colors[count - 1])
                map.draw_lines(room2, room1, color=colors[count - 1], make_stairs=True, stairway=stair)
            else:
                print("Making lines")
                # time.sleep(5)
                map.draw_lines(room2, room1, color=colors[count - 1])

def main(new_user=None):
    """Creates the submit button and waits for the user to submit"""

    global guest
    if new_user == 'guest':
        guest = new_user

    submit_btn = tk.Button(root, text="Submit", width=10, height=2, command=submit)
    submit_btn.grid(row=0, column=3)
    root.mainloop()


if __name__ == '__main__':
    main()
