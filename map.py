"""Generates a map of the school and makes a path that shows where to go"""

#!/usr/bin/python
# map.py
__author__ = "Elijah"
__version__ = 3.7

import tkinter as tk
import math
import datetime


current_time = datetime.datetime.now()
day = current_time.weekday()
# day = 4

width   = 1450
height  = 765
x_shift = 0
y_shift = 0

root = tk.Tk()
root.geometry("%dx%d+%d+%d" % (width, height, x_shift, y_shift))
root.title("Map")

previous_class = ""

img1 = tk.PhotoImage(file="CCHS_floor1.gif", master=root)
img2 = tk.PhotoImage(file="CCHS_floor2.gif", master=root)

canvas = tk.Canvas(root, width=width, height=height)
canvas.create_image(0, 0, image=img1, anchor='nw')
canvas.create_image(1100, 350, image=img2)
canvas.config(cursor="circle")
canvas.pack()

coords1 = [[118, 520, 239, 638],
           [273, 520, 394, 560],
           [241, 607, 280, 637],
           [282, 607, 386, 637],
           [444, 552, 533, 616],
           [448, 520, 550, 550],
           [427, 404, 458, 469],
           [460, 405, 518, 452],
           [520, 404, 550, 463],
           [110, 520, 117, 550],
           [240, 565, 247, 595],
           [420, 565, 427, 595],
           [550, 520, 557, 550]]

coords2 = [[394, 268, 428, 309],
           [430, 280, 487, 309],
           [493, 280, 550, 309],
           [552, 268, 585, 309],
           [535, 215, 550, 256],
           [567, 139, 600, 190],
           [444, 169, 533, 256],
           [110, 139, 117, 169],
           [249, 183, 263, 218],
           [405, 183, 418, 218],
           [550, 139, 558, 169]]

coords3 = [[827, 505, 851, 548],
           [836, 550, 852, 579],
           [853, 505, 884, 537],
           [886, 503, 914, 537],
           [916, 503, 986, 537],
           [988, 503, 1006, 537],
           [1008, 504, 1038, 537],
           [1040, 503, 1069, 537],
           [1071, 503, 1129, 537],
           [1132, 503, 1159, 537],
           [1162, 503, 1192, 537],
           [1194, 503, 1211, 537],
           [1283, 503, 1313, 537],
           [1315, 505, 1346, 536],
           [1348, 505, 1371, 547],
           [1346, 549, 1362, 579],
           [1348, 581, 1371, 623],
           [1315, 591, 1346, 623],
           [1283, 591, 1313, 624],
           [1254, 591, 1281, 624],
           [1224, 591, 1252, 624],
           [1193, 591, 1222, 624],
           [1161, 591, 1191, 623],
           [1130, 590, 1158, 624],
           [1100, 590, 1128, 624],
           [1069, 590, 1098, 624],
           [1039, 590, 1067, 624],
           [1007, 591, 1037, 624],
           [977, 590, 1005, 624],
           [947, 590, 975, 624],
           [915, 590, 945, 624],
           [885, 590, 913, 624],
           [853, 591, 883, 622],
           [827, 590, 851, 622],
           [853, 556, 876, 572],
           [1015, 548, 1031, 579],
           [1169, 548, 1184, 579],
           [1346, 571, 1322, 554]]

coords4 = [[827, 135, 878, 165],
           [837, 177, 852, 208],
           [886, 132, 940, 166],
           [951, 132, 1006, 166],
           [1008, 133, 1038, 166],
           [1040, 132, 1069, 166],
           [1071, 132, 1099, 166],
           [1101, 132, 1129, 166],
           [1132, 132, 1159, 166],
           [1162, 133, 1192, 166],
           [1194, 132, 1222, 166],
           [1224, 132, 1283, 166],
           [1269, 177, 1313, 209],
           [1285, 132, 1313, 166],
           [1321, 134, 1372, 164],
           [1343, 177, 1362, 208],
           [1321, 221, 1372, 252],
           [1260, 219, 1313, 253],
           [1193, 219, 1248, 253],
           [1162, 219, 1191, 252],
           [1106, 219, 1160, 253],
           [1039, 219, 1094, 253],
           [1008, 219, 1037, 251],
           [952, 219, 1006, 253],
           [885, 219, 942, 253],
           [828, 221, 878, 251],
           [853, 184, 876, 201],
           [1015, 177, 1031, 209],
           [1169, 177, 1184, 209],
           [1323, 184, 1342, 201]]

###########
##FLOOR 1##
###########
room111 = canvas.create_rectangle(coords1[0])
room112 = canvas.create_rectangle(coords1[1])
room121 = canvas.create_rectangle(coords1[2])
room122 = canvas.create_rectangle(coords1[3])
room130 = canvas.create_rectangle(coords1[4])
room131 = canvas.create_rectangle(coords1[5])
room138 = canvas.create_rectangle(coords1[6])
room140 = canvas.create_rectangle(coords1[7])
room141 = canvas.create_rectangle(coords1[8])

stairway_11 = canvas.create_rectangle(coords1[9])
stairway_12 = canvas.create_rectangle(coords1[10])
stairway_13 = canvas.create_rectangle(coords1[11])
stairway_14 = canvas.create_rectangle(coords1[12])

stairways1 = {0: stairway_11, 1: stairway_12, 2: stairway_13, 3: stairway_14}

floor1 = {111: room111, 112: room112, 121: room121, 122: room122, 130: room130, 131: room131,
          138: room138, 140: room140, 141: room141}

###########
##FLOOR 2##
###########
room248 = canvas.create_rectangle(coords2[0])
room253 = canvas.create_rectangle(coords2[1])
room254 = canvas.create_rectangle(coords2[2])
room256 = canvas.create_rectangle(coords2[3])
room257 = canvas.create_rectangle(coords2[4])
room261 = canvas.create_rectangle(coords2[5])
room262 = canvas.create_rectangle(coords2[6])

stairway_21 = canvas.create_rectangle(coords2[7])
stairway_22 = canvas.create_rectangle(coords2[8])
stairway_23 = canvas.create_rectangle(coords2[9])
stairway_24 = canvas.create_rectangle(coords2[10])

stairways2 = {0: stairway_21, 1: stairway_22, 2: stairway_23, 3: stairway_24}

floor2 = {248: room248, 253: room253, 254: room254, 256: room256, 257: room257, 261: room261,
          262: room262}

###########
##FLOOR 3##
###########
room301 = canvas.create_rectangle(coords3[0])
room302 = canvas.create_rectangle(coords3[1])
room303 = canvas.create_rectangle(coords3[2])
room305 = canvas.create_rectangle(coords3[3])
room306 = canvas.create_rectangle(coords3[4])
room309 = canvas.create_rectangle(coords3[5])
room311 = canvas.create_rectangle(coords3[6])
room314 = canvas.create_rectangle(coords3[7])
room316 = canvas.create_rectangle(coords3[8])
room318 = canvas.create_rectangle(coords3[9])
room320 = canvas.create_rectangle(coords3[10])
room322 = canvas.create_rectangle(coords3[11])
room325 = canvas.create_rectangle(coords3[12])
room326 = canvas.create_rectangle(coords3[13])
room327 = canvas.create_rectangle(coords3[14])
room328 = canvas.create_rectangle(coords3[15])
room329 = canvas.create_rectangle(coords3[16])
room330 = canvas.create_rectangle(coords3[17])
room332 = canvas.create_rectangle(coords3[18])
room333 = canvas.create_rectangle(coords3[19])
room334 = canvas.create_rectangle(coords3[20])
room335 = canvas.create_rectangle(coords3[21])
room337 = canvas.create_rectangle(coords3[22])
room339 = canvas.create_rectangle(coords3[23])
room340 = canvas.create_rectangle(coords3[24])
room341 = canvas.create_rectangle(coords3[25])
room343 = canvas.create_rectangle(coords3[26])
room346 = canvas.create_rectangle(coords3[27])
room348 = canvas.create_rectangle(coords3[28])
room349 = canvas.create_rectangle(coords3[29])
room350 = canvas.create_rectangle(coords3[30])
room351 = canvas.create_rectangle(coords3[31])
room353 = canvas.create_rectangle(coords3[32])
room354 = canvas.create_rectangle(coords3[33])

stairway_31 = canvas.create_rectangle(coords3[34])
stairway_32 = canvas.create_rectangle(coords3[35])
stairway_33 = canvas.create_rectangle(coords3[36])
stairway_34 = canvas.create_rectangle(coords3[37])

stairways3 = {0: stairway_31, 1: stairway_32, 2: stairway_33, 3: stairway_34}

floor3 = {301: room301, 302: room302, 303: room303, 305: room305, 306: room306, 309: room309,
          311: room311, 314: room314, 316: room316, 318: room318, 320: room320, 322: room322,
          325: room325, 326: room326, 327: room327, 328: room328, 329: room329, 330: room330,
          332: room332, 333: room333, 334: room334, 335: room335, 337: room337, 339: room339,
          340: room340, 341: room341, 343: room343, 346: room346, 348: room348, 349: room349,
          350: room350, 351: room351, 353: room353, 354: room354}

###########
##FLOOR 4##
###########
room401 = canvas.create_rectangle(coords4[0])
room402 = canvas.create_rectangle(coords4[1])
room404 = canvas.create_rectangle(coords4[2])
room408 = canvas.create_rectangle(coords4[3])
room411 = canvas.create_rectangle(coords4[4])
room412 = canvas.create_rectangle(coords4[5])
room415 = canvas.create_rectangle(coords4[6])
room418 = canvas.create_rectangle(coords4[7])
room419 = canvas.create_rectangle(coords4[8])
room420 = canvas.create_rectangle(coords4[9])
room423 = canvas.create_rectangle(coords4[10])
room424 = canvas.create_rectangle(coords4[11])
room426 = canvas.create_rectangle(coords4[12])
room427 = canvas.create_rectangle(coords4[13])
room429 = canvas.create_rectangle(coords4[14])
room430 = canvas.create_rectangle(coords4[15])
room431 = canvas.create_rectangle(coords4[16])
room435 = canvas.create_rectangle(coords4[17])
room436 = canvas.create_rectangle(coords4[18])
room438 = canvas.create_rectangle(coords4[19])
room440 = canvas.create_rectangle(coords4[20])
room441 = canvas.create_rectangle(coords4[21])
room443 = canvas.create_rectangle(coords4[22])
room445 = canvas.create_rectangle(coords4[23])
room446 = canvas.create_rectangle(coords4[24])
room449 = canvas.create_rectangle(coords4[25])

stairway_41 = canvas.create_rectangle(coords4[26])
stairway_42 = canvas.create_rectangle(coords4[27])
stairway_43 = canvas.create_rectangle(coords4[28])
stairway_44 = canvas.create_rectangle(coords4[29])

stairways4 = {0: stairway_41, 1: stairway_42, 2: stairway_43, 3: stairway_44}

floor4 = {401: room401, 402: room402, 404: room404, 408: room408, 411: room411, 412: room412,
          415: room415, 418: room418, 419: room419, 420: room420, 423: room423, 424: room424,
          426: room426, 427: room427, 429: room429, 430: room430, 431: room431, 435: room435,
          436: room436, 438: room438, 440: room440, 441: room441, 443: room443, 445: room445,
          446: room446, 449: room449}


def draw_lines(first_room, second_room, color=None, make_stairs=False, stairway=None):
    """Draws a line from the two coordinates

    :param first_room: the number of the first room
    :param second_room: the number of the second room
    :param color: the color of the line (if none, default is blue)
    :param make_stairs: True if the program needs to know which staircase to use
    :param stairway: a list with the staircase number
    :return: False if room doesn't exist"""

    thing = ""
    if not make_stairs:
        stairway = []

    print("Rooms:", first_room, second_room)

    if "Advisory" in first_room:
        room1 = 426
        room2 = int(second_room[-3:])
    elif "Advisory" in second_room:
        room1 = int(first_room[-3:])
        room2 = 426
    elif "Lunch" in first_room:
        room1 = 411
        room2 = int(second_room[-3:])
    elif "Lunch" in second_room:
        room1 = int(first_room[-3:])
        room2 = 411
    else:
        room1 = int(first_room[-3:])
        room2 = int(second_room[-3:])

    diff_floor   = False
    first_floor  = False
    second_floor = False
    third_floor  = False
    fourth_floor = False

    if room1 in floor1:
        first_floor = True
        if room2 not in floor1:
            diff_floor = True

    elif room1 in floor2:
        second_floor = True
        if room2 not in floor2:
            diff_floor = True

    elif room1 in floor3:
        third_floor = True
        if room2 not in floor3:
            diff_floor = True

    elif room1 in floor4:
        fourth_floor = True
        if room2 not in floor4:
            diff_floor = True

    if not diff_floor:
        if first_floor:
            room1 = floor1[room1]
            room2 = floor1[room2]
        elif second_floor:
            room1 = floor2[room1]
            room2 = floor2[room2]
        elif third_floor:
            room1 = floor3[room1]
            room2 = floor3[room2]
        elif fourth_floor:
            room1 = floor4[room1]
            room2 = floor4[room2]
        else:
            return False
        x1, y1, x2, y2 = canvas.coords(room1)
        x3, y3, x4, y4 = canvas.coords(room2)
    else:
        if first_floor:
            if make_stairs:
                thing = "1" + stairway
                stairway = [int(thing)]

            room1 = floor1[room1]
            print(room1)

        elif second_floor:
            if make_stairs:
                thing = "2" + stairway
                stairway = [int(thing)]

            room1 = floor2[room1]
        elif third_floor:
            if make_stairs:
                thing = "3" + stairway
                stairway = [int(thing)]

            room1 = floor3[room1]
        elif fourth_floor:
            if make_stairs:
                thing = "4" + stairway
                stairway = [int(thing)]

            room1 = floor4[room1]
        else:
            return False

        x1, y1, x2, y2 = canvas.coords(room1)
        x_dist = (math.sqrt((x2 - x1) ** 2)) // 2
        x_distance = x2 - x_dist

        x3 = 0
        y3 = 0
        x4 = 0
        y4 = 0

        #determines closest stairway
        if make_stairs:
            pass
        elif first_floor:
            old_stairway = stairways1[0]
            for i in range(4):
                stair = stairways1[i]
                if i == 0:
                    x3, y3, x4, y4 = canvas.coords(stair)
                else:
                    x5, y5, x6, y6 = canvas.coords(stair)
                    x_distance1 = (math.sqrt((x4 - x3) ** 2)) // 2
                    x_distance2 = (math.sqrt((x6 - x5) ** 2)) // 2

                    x_dist1 = x4 - x_distance1
                    x_dist2 = x6 - x_distance2

                    if abs(x_distance - x_dist1) > abs(x_distance - x_dist2):
                        stairway = [stair]
                        x3, y3, x4, y4 = canvas.coords(stair)
                        old_stairway = stair

                    else:
                        stairway = [old_stairway]

        elif second_floor:
            old_stairway = stairways2[0]
            for i in range(4):
                stair = stairways2[i]
                if i == 0:
                    x3, y3, x4, y4 = canvas.coords(stair)
                else:
                    x5, y5, x6, y6 = canvas.coords(stair)
                    x_distance1 = (math.sqrt((x4 - x3) ** 2)) // 2
                    x_distance2 = (math.sqrt((x6 - x5) ** 2)) // 2

                    x_dist1 = x4 - x_distance1
                    x_dist2 = x6 - x_distance2

                    if abs(x_distance - x_dist1) > abs(x_distance - x_dist2):
                        stairway = [stair]
                        x3, y3, x4, y4 = canvas.coords(stair)
                        old_stairway = stair

                    else:
                        stairway = [old_stairway]

        elif third_floor:
            old_stairway = stairways3[0]
            for i in range(4):
                stair = stairways3[i]
                if i == 0:
                    x3, y3, x4, y4 = canvas.coords(stair)
                else:
                    x5, y5, x6, y6 = canvas.coords(stair)
                    x_distance1 = (math.sqrt((x4 - x3) ** 2)) // 2
                    x_distance2 = (math.sqrt((x6 - x5) ** 2)) // 2

                    x_dist1 = x4 - x_distance1
                    x_dist2 = x6 - x_distance2

                    if abs(x_distance - x_dist1) > abs(x_distance - x_dist2):
                        stairway = [stair]
                        x3, y3, x4, y4 = canvas.coords(stair)
                        old_stairway = stair

                    else:
                        stairway = [old_stairway]

        elif fourth_floor:
            old_stairway = stairways4[0]
            for i in range(4):
                stair = stairways4[i]
                if i == 0:
                    x3, y3, x4, y4 = canvas.coords(stair)
                else:
                    x5, y5, x6, y6 = canvas.coords(stair)
                    x_distance1 = (math.sqrt((x4 - x3) ** 2)) // 2
                    x_distance2 = (math.sqrt((x6 - x5) ** 2)) // 2

                    x_dist1 = x4 - x_distance1
                    x_dist2 = x6 - x_distance2

                    if abs(x_distance - x_dist1) > abs(x_distance - x_dist2):
                        stairway.append(stair)
                        x3, y3, x4, y4 = canvas.coords(stair)
                        old_stairway = stair
                    else:
                        stairway.append(old_stairway)

        #determines the middle of each room and the distance between them
        print("Stairway:", stairway)
        staircase = stairway[len(stairway) - 1]
        x3, y3, x4, y4 = canvas.coords(staircase)

    x_distance1 = (math.sqrt((x2 - x1) ** 2)) // 2
    y_distance1 = (math.sqrt((y2 - y1) ** 2)) // 2
    x_distance2 = (math.sqrt((x4 - x3) ** 2)) // 2
    y_distance2 = (math.sqrt((y4 - y3) ** 2)) // 2

    x_dist1 = x2 - x_distance1
    y_dist1 = y2 - y_distance1

    x_dist2 = x4 - x_distance2
    y_dist2 = y4 - y_distance2

    amt  = 22
    dist = 22
    midpoint1 = 580
    midpoint2 = 200
    size = 3

    #flips the y coords if they are on the other side
    switch1 = False
    switch2 = False
    print(y1, y2, y3, y4)

    print(room1, room2)
    if first_floor or third_floor:
        if y1 > midpoint1 and y2 > midpoint1:
            switch1 = True
        if y3 > midpoint1 and y4 > midpoint1:
            switch2 = True

    if second_floor or fourth_floor:
        if y1 > midpoint2 and y2 > midpoint2:
            switch1 = True
        if y3 > midpoint2 and y4 > midpoint2:
            switch2 = True

    if color is None:
        color = "blue"

    print(switch1, switch2, color)
    print()

    if switch1:
        canvas.create_line(x_dist1, y_dist1, x_dist1, y_dist1 - amt, width=size, fill=color)
    else:
        canvas.create_line(x_dist1, y_dist1, x_dist1, y_dist1 + amt, width=size, fill=color)


    if not make_stairs:
        return str(stairway)[2:3]

# def make_point(event):
#     """Creates a point at where the place was clicked
#
#     :param event: the coordinates of the place that was clicked
#     :return: None"""
#
#     x = event.x
#     y = event.y
#
#     num = 1
#
#     canvas.create_oval(x - num, y - num, x + num, y + num, fill="black")
#     print(x, y)

# def make_stuff(event=None):
#     """Calls the method to draw lines on the map
#
#     :param event: None
#     :return: None"""
#
#     if day == 0:
#         draw_lines("room411", "room111", "red")
#         draw_lines("room111", "room411", "red")
#         draw_lines("room111", "room348", "orange")
#         draw_lines("room348", "room111", "orange")
#         draw_lines("room348", "room318", "blue")
#         draw_lines("room318", "room348", "blue")
#         draw_lines("room318", "room329", "green")
#         draw_lines("room329", "room318", "green")
#         draw_lines("room329", "room112", "purple")
#         draw_lines("room112", "room329", "purple")
#         draw_lines("room112", "room435", "black")
#         draw_lines("room435", "room112", "black")
#
#     elif day == 1:
#         draw_lines("room411", "room111", "red")
#         draw_lines("room111", "room411", "red")
#         draw_lines("room111", "room415", "orange")
#         draw_lines("room415", "room111", "orange")
#         draw_lines("room415", "room318", "blue")
#         draw_lines("room318", "room415", "blue")
#         draw_lines("room318", "room329", "green")
#         draw_lines("room329", "room318", "green")
#         draw_lines("room329", "room112", "purple")
#         draw_lines("room112", "room329", "purple")
#         draw_lines("room112", "room435", "black")
#         draw_lines("room435", "room112", "black")
#
#     elif day == 2:
#         draw_lines("room411", "room111", "red")
#         draw_lines("room111", "room411", "red")
#         draw_lines("room111", "room426", "orange")
#         draw_lines("room426", "room111", "orange")
#         draw_lines("room426", "room348", "green")
#         draw_lines("room348", "room426", "green")
#         draw_lines("room348", "room318", "blue")
#         draw_lines("room318", "room348", "blue")
#         draw_lines("room318", "room329", "purple")
#         draw_lines("room329", "room318", "purple")
#         draw_lines("room329", "room112", "black")
#         draw_lines("room112", "room329", "black")
#         draw_lines("room112", "room415", "brown")
#         draw_lines("room415", "room112", "brown")
#
#     elif day == 3:
#         draw_lines("room411", "room348", "red")
#         draw_lines("room348", "room411", "red")
#         draw_lines("room348", "room415", "orange")
#         draw_lines("room415", "room348", "orange")
#         draw_lines("room415", "room318", "green")
#         draw_lines("room318", "room415", "green")
#         draw_lines("room318", "room329", "blue")
#         draw_lines("room329", "room112", "blue")
#         draw_lines("room329", "room112", "purple")
#         draw_lines("room112", "room435", "black")
#         draw_lines("room435", "room112", "black")
#
#     elif day == 4:
#         draw_lines("room111", "room348", "red")
#         draw_lines("room348", "room111", "red")
#         draw_lines("room348", "room415", "orange")
#         draw_lines("room415", "room348", "orange")
#         draw_lines("room415", "room318", "green")
#         draw_lines("room318", "room415", "green")
#         draw_lines("room318", "room329", "blue")
#         draw_lines("room329", "room318", "blue")
#         draw_lines("room329", "room112", "purple")
#         draw_lines("room112", "room329", "purple")
#         draw_lines("room112", "room435", "black")
#         draw_lines("room435", "room112", "black")

def main():
    """Runs the program

    :return: None"""

    # canvas.bind("<Button-1>", make_point)
    # root.bind("<Key>", make_stuff)
    root.mainloop()


if __name__ == '__main__':
    main()
