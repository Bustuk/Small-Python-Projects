import tkinter as tk
import turtle


master = tk.Tk()
master.geometry('750x598+50+50')
master.title('Turtle Graphic GUI')
canvas = tk.Canvas(master, height=600, width=600)
canvas.grid(column=0,row=0)

turt = turtle.RawTurtle(canvas)
turt.screen.bgcolor('grey')
buttons_frame = tk.Frame(master, bg='black', width=150, height=600)
buttons_frame.grid_propagate(0)
buttons_frame.grid(column=1, row=0)
buttons_frame.grid_propagate(0)

distance = 25


def move_forward():
    global distance
    turt.forward(distance)


def move_backward():
    global distance
    turt.backward(distance)


def turn_left():
    global distance
    turt.left(90)


def turn_right():
    global distance
    turt.right(90)


list_of_colors = {0: "white", 1: "black", 2 :"red", 3: "green", 4: "blue", 5: "cyan", 6: "yellow", 7: 'grey',
                 8: 'white smoke', 9: 'DarkOrchid4', 10: 'salmon', 11: 'orange', 12: 'gold4', 13: 'maroon4'}

list_of_shapes = {0: "arrow", 1: "triangle",  2: "turtle", 3: "circle", 4: "square", 5: "classic"}
number_of_changes_in_shapes = 0
number_of_changes_in_colors = 0
number_of_changes_in_bgcolors = 0

def change_bgcolor():
    global number_of_changes_in_bgcolors
    global list_of_colors
    turt.screen.bgcolor(list_of_colors[number_of_changes_in_bgcolors % 14])
    number_of_changes_in_bgcolors += 1


def change_color():
    global number_of_changes_in_colors
    global list_of_colors
    turt.color(list_of_colors[number_of_changes_in_colors % 14])
    number_of_changes_in_colors += 1


def change_shape():
    global list_of_shapes
    global number_of_changes_in_shapes
    turt.shape(list_of_shapes[number_of_changes_in_shapes % 6])
    number_of_changes_in_shapes += 1


def change_line_size_down():
    x = turt.pensize()

    if x > 0.5:
        turt.pensize(x - 0.5)
    else:
        button_line_size_down['state'] = 'disabled'


def change_line_size_up():
    x = turt.pensize()
    turt.pensize(x+0.5)
    button_line_size_down['state'] = 'normal'


def change_pen_size_down():
    size = turt.turtlesize()
    size = list(size)

    if size[0] > 0.5:
        a = size[0] - 0.5
        b = size[1] - 0.5
        turt.turtlesize(stretch_len=a, stretch_wid=b)
    else:
        button_pen_size_down['state'] = 'disabled'


def change_pen_size_up():
    size = turt.turtlesize()
    increase = tuple([1 + num for num in size])
    turt.turtlesize(*increase)
    button_pen_size_down['state'] = 'normal'


def move_length_change():
    global distance
    distance = float(length_enter.get())


def pendown():
    turt.pendown()
    button_pen__up['state'] = 'normal'
    button_pen__down['state'] = 'disabled'


def penup():
    turt.penup()
    button_pen__up['state'] = 'disabled'
    button_pen__down['state'] = 'normal'


def draw_circle():
    global distance
    turt.circle(distance)


button_forward = tk.Button(buttons_frame, height=5, text='GO\nFORWARD', command=move_forward, width=9, bd=3)
button_forward.grid(row=2, column=0)

button_backward = tk.Button(buttons_frame, height=5, text='GO\nBACKWARD', command=move_backward, width=9, bd=3)
button_backward.grid(row=2, column=1)

button_left = tk.Button(buttons_frame, height=5, text='TURN\nLEFT', command=turn_left, width=9, bd=3)
button_left.grid(row=3, column=0)

button_right = tk.Button(buttons_frame, height=5, text='TURN\nRIGHT', command=turn_right, width=9, bd=3)
button_right.grid(row=3, column=1)

button_change_shape = tk.Button(buttons_frame, height=3, text='CHANGE\nSHAPE', command=change_shape, width=9, bd=3)
button_change_shape.grid(row=5, column=0)

button_change_size = tk.Button(buttons_frame, height=3, text='CHANGE\nCOLOR', command=change_color, width=9, bd=3)
button_change_size.grid(row=5, column=1)

button_line_size_up = tk.Button(buttons_frame, height=3, text='LINE SIZE\nUP', command=change_line_size_up, width=9, bd=3)
button_line_size_up.grid(row=7, column=0)

button_line_size_down = tk.Button(buttons_frame, height=3, text='LINE SIZE\nDOWN', command=change_line_size_down, width=9, bd=3)
button_line_size_down.grid(row=7, column=1)

button_pen_size_up = tk.Button(buttons_frame, height=3, text='PEN SIZE\nUP', command=change_pen_size_up, width=9, bd=3)
button_pen_size_up.grid(row=6, column=0)

button_pen_size_down = tk.Button(buttons_frame, height=3, text='PEN SIZE\nDOWN', command=change_pen_size_down, width=9, bd=3)
button_pen_size_down.grid(row=6, column=1)

button_pen__up = tk.Button(buttons_frame, height=3, text='NO-DRAW\nMODE', command=penup, width=9, bd=3)
button_pen__up.grid(row=9, column=1)

button_pen__down = tk.Button(buttons_frame, height=3, text='DRAW\nMODE', command=pendown, width=9, bd=3)
button_pen__down.grid(row=9, column=0)


button_stamp = tk.Button(buttons_frame, height=3, text='STAMP', command=turt.stamp, width=9, bd=3)
button_stamp.grid(row=4, column=0)

button_draw_circle = tk.Button(buttons_frame, height=3, text='DRAW\nCIRCLE', command=draw_circle, width=9, bd=3)
button_draw_circle.grid(row=4, column=1)

button_clear = tk.Button(buttons_frame, height=3, text='CLEARN\nCANVAS', command=turt.clear, width=9, bd=3)
button_clear.grid(row=8, column=0)

button_clear = tk.Button(buttons_frame, height=3, text='CANVAS\nCOLOR', command=change_bgcolor, width=9, bd=3)
button_clear.grid(row=8, column=1)


frame_for_length = tk.Frame(buttons_frame, width=180, height=100, bd=1)
frame_for_length.grid(columnspan=2, row=1)


length_label = tk.Label(frame_for_length, text="Enter move length")
length_label.pack_propagate(0)
length_label.pack(expand=1, fill='x')

ok_button = tk.Button(frame_for_length, text='ok', command=move_length_change)
ok_button.pack(side=tk.RIGHT)

length_enter = tk.Entry(frame_for_length)
length_enter.pack(side=tk.LEFT, fill='y')
length_enter.pack_propagate()


control_panel_label = tk.Label(buttons_frame, text='        CONTROL PANEL        ',bd=3)
control_panel_label.grid(row=0, columnspan=2)
control_panel_label.grid_propagate()


master.mainloop()