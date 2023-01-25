#imports
import math
from tkinter import *
from playsound import playsound
from threading import Thread

#set variable
display_value = ""

#tool functions
def new_window(minx, miny, title, background_color, iconfile): #return a window
    new_window = Tk()
    new_window.minsize(minx, miny)
    new_window.title(title)
    new_window.config(bg=background_color)
    new_window.iconphoto(True, PhotoImage(file=iconfile))
    return new_window

#functions
def sound_play():
    playsound('assets\\calculator_key_press_sound_1.mp3')

def set_char(char):
    Tsound_play = Thread(target=sound_play, args=[], daemon=True)
    Tsound_play.start()
    global display_value
    display_value = display_value + str(char)
    display_calculator_label.config(text=display_value)
def backspace():
    Tsound_play = Thread(target=sound_play, args=[], daemon=True)
    Tsound_play.start()
    global display_value
    display_value = display_value[0:len(display_value)-1]
    display_calculator_label.config(text=display_value)
def clear():
    Tsound_play = Thread(target=sound_play, args=[], daemon=True)
    Tsound_play.start()
    global display_value
    display_value = ""
    display_calculator_label.config(text=display_value)
def equal():
    Tsound_play = Thread(target=sound_play, args=[], daemon=True)
    Tsound_play.start()
    global display_value
    try:
        display_value = str(eval(display_value))
        display_calculator_label.config(text=display_value)
    except ZeroDivisionError:
        display_value = "Arithmetic Error"
        display_calculator_label.config(text=display_value)
    except SyntaxError:
        display_value = "Arithmetic Impossible"
        display_calculator_label.config(text=display_value)

def power():
    Tsound_play = Thread(target=sound_play, args=[], daemon=True)
    Tsound_play.start()
    equal()
    global display_value
    display_value = str(float(display_value)*float(display_value))
    display_calculator_label.config(text=display_value)
def square():
    Tsound_play = Thread(target=sound_play, args=[], daemon=True)
    Tsound_play.start()
    equal()
    global display_value
    display_value = str(math.sqrt(float(display_value)))
    display_calculator_label.config(text=display_value)
def ratio():
    Tsound_play = Thread(target=sound_play, args=[], daemon=True)
    Tsound_play.start()
    equal()
    global display_value
    display_value = f"{float(display_value)*100}%"
    display_calculator_label.config(text=display_value)

def input_process(event):
    command = {
        "0": lambda: set_char("0"),
        "1":lambda: set_char(1),
        "2": lambda: set_char(2),
        "3":lambda: set_char(3),
        "4": lambda: set_char(4),
        "5": lambda: set_char(5),
        "6": lambda: set_char(6),
        "7": lambda: set_char(7),
        "8": lambda: set_char(8),
        "9": lambda: set_char(9),
        "plus": lambda: set_char('+'),
        "minus": lambda: set_char('-'),
        "asterisk": lambda: set_char('*'),
        "slash": lambda: set_char('/'),
        "Return": lambda: equal(),
        "comma": lambda: set_char('.'),
        "period": lambda: set_char('.'),
        "BackSpace": backspace
    }
    command[event.keysym]()
def get_keyboard_input():
    window.bind("<Key>", input_process)

#set window
window = new_window(600, 700, 'Calculator', '#E8E288', 'assets\\icon.png')

#set calculator frame
main_calculator_frame = Frame(window, width=600, height=700, relief=GROOVE, background='#00fff5', bd=5)
item_calculator_frame = Frame(main_calculator_frame, width=550, height=650, background='#00fff5')
display_calculator_frame = Frame(item_calculator_frame, width=549, height=150, background='#00b3ac', relief=GROOVE, bd=3)
keyboard_calculator_frame = Frame(item_calculator_frame, width=549, height=475, background='#00fff5')
number_pad_calculator_frame = Frame(keyboard_calculator_frame, width=390, height=474, background='#00fff5')
operation_pad_calculator_frame = Frame(keyboard_calculator_frame, width=137, height=474, background='#00fff5')

#display calculator label
display_calculator_label = Label(display_calculator_frame, text=display_value, font=('Cambria', 30), background='#00b3ac')

#set buttons
sum_button_photo = PhotoImage(file='assets\\sum_button_photo.png')
sum_button = Button(operation_pad_calculator_frame, width=129, height=93, image=sum_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = lambda: set_char('+'))
sub_button_photo = PhotoImage(file='assets\\sub_button_photo.png')
sub_button = Button(operation_pad_calculator_frame, width=129, height=93, image=sub_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = lambda: set_char('-'))
mult_button_photo = PhotoImage(file='assets\\mult_button_photo.png')
mult_button = Button(operation_pad_calculator_frame, width=129, height=93, image=mult_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = lambda: set_char('*'))
div_button_photo = PhotoImage(file='assets\\div_button_photo.png')
div_button = Button(operation_pad_calculator_frame, width=129, height=93, image=div_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = lambda: set_char('/'))
equal_button_photo = PhotoImage(file='assets\\equal_button_photo.png')
equal_button = Button(operation_pad_calculator_frame, width=129, height=93, image=equal_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = equal)

backspace_button_photo = PhotoImage(file='assets\\backspace_button_photo.png')
backspace_button = Button(number_pad_calculator_frame, width=93, height=114, image=backspace_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = backspace)
pow_button_photo = PhotoImage(file='assets\\pow_button_photo.png')
pow_button = Button(number_pad_calculator_frame, width=93, height=114, image=pow_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = power)
square_button_photo = PhotoImage(file='assets\\square_button_photo.png')
square_button = Button(number_pad_calculator_frame, width=93, height=114, image=square_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = square)
c_button_photo = PhotoImage(file='assets\\c_button_photo.png')
c_button = Button(number_pad_calculator_frame, width=93, height=114, image=c_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = clear)

ratio_button_photo = PhotoImage(file='assets\\ratio_button_photo.png')
ratio_button = Button(number_pad_calculator_frame, width=93, height=114, image=ratio_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = ratio)
n7_button_photo = PhotoImage(file='assets\\n7_button_photo.png')
n7_button = Button(number_pad_calculator_frame, width=93, height=114, image=n7_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = lambda: set_char(7))
n8_button_photo = PhotoImage(file='assets\\n8_button_photo.png')
n8_button = Button(number_pad_calculator_frame, width=93, height=114, image=n8_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = lambda: set_char(8))
n9_button_photo = PhotoImage(file='assets\\n9_button_photo.png')
n9_button = Button(number_pad_calculator_frame, width=93, height=114, image=n9_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = lambda: set_char(9))

comma_button_photo = PhotoImage(file='assets\\comma_button_photo.png')
comma_button = Button(number_pad_calculator_frame, width=93, height=114, image=comma_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = lambda: set_char('.'))
n4_button_photo = PhotoImage(file='assets\\n4_button_photo.png')
n4_button = Button(number_pad_calculator_frame, width=93, height=114, image=n4_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = lambda: set_char(4))
n5_button_photo = PhotoImage(file='assets\\n5_button_photo.png')
n5_button = Button(number_pad_calculator_frame, width=93, height=114, image=n5_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = lambda: set_char(5))
n6_button_photo = PhotoImage(file='assets\\n6_button_photo.png')
n6_button = Button(number_pad_calculator_frame, width=93, height=114, image=n6_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = lambda: set_char(6))

n0_button_photo = PhotoImage(file='assets\\n0_button_photo.png')
n0_button = Button(number_pad_calculator_frame, width=93, height=114, image=n0_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = lambda: set_char(0))
n1_button_photo = PhotoImage(file='assets\\n1_button_photo.png')
n1_button = Button(number_pad_calculator_frame, width=93, height=114, image=n1_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = lambda: set_char(1))
n2_button_photo = PhotoImage(file='assets\\n2_button_photo.png')
n2_button = Button(number_pad_calculator_frame, width=93, height=114, image=n2_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = lambda: set_char(2))
n3_button_photo = PhotoImage(file='assets\\n3_button_photo.png')
n3_button = Button(number_pad_calculator_frame, width=93, height=114, image=n3_button_photo, background='#3CDBD3', relief=GROOVE, bd=3, activebackground='#50CEC8', command = lambda: set_char(3))

#program
if __name__ == '__main__':
    main_calculator_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    item_calculator_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    display_calculator_frame.place(relx=0, rely=0)
    keyboard_calculator_frame.place(relx=0, rely=0.27)
    number_pad_calculator_frame.place(relx=0, rely=0)
    operation_pad_calculator_frame.place(relx=0.75, rely=0)

    display_calculator_label.place(relx=0.95, rely=0.5, anchor=E)

    sum_button.place(x=0, y=0)
    sub_button.place(x=0, y=97)
    mult_button.place(x=0, y=188)
    div_button.place(x=0, y=282)
    equal_button.place(x=0, y=375)

    backspace_button.place(x=0, y=0)
    pow_button.place(x=97, y=0)
    square_button.place(x=194,y=0)
    c_button.place(x=291, y=0)

    ratio_button.place(x=0, y=118)
    n7_button.place(x=97, y=118)
    n8_button.place(x=194,y=118)
    n9_button.place(x=291, y=118)

    comma_button.place(x=0, y=236)
    n4_button.place(x=97, y=236)
    n5_button.place(x=194,y=236)
    n6_button.place(x=291, y=236)

    n0_button.place(x=0, y=354)
    n1_button.place(x=97, y=354)
    n2_button.place(x=194,y=354)
    n3_button.place(x=291, y=354)

    get_keyboard_input()

    window.mainloop()
