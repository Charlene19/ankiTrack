from tkinter import IntVar

from tkinter import *
from datetime import date
# create Tk window
root = Tk()
today = date.today()
print("Today's date:", today)
# set name of window
root.title('Testing Values')

# initalise values from user (spinbox values)
item_1 = IntVar()
item_2 = IntVar()
item_1 = Spinbox(root, from_=0, to=10, width=5)
item_1.grid(row=0, column=0)
a = item_1.get()


def print_item_values():
    nvalue = int(item_1.get()) + int(item_2.get())
    print(int(item_1.get()) + int(item_2.get()))
    print(nvalue)

# item 1 spinbox
item_1 = Spinbox(root, from_=0, to=10, width=5)
item_1.grid(row=0, column=0)
# item 1 spinbox
item_2 = Spinbox(root, from_=0, to=10, width=5)
item_2.grid(row=1, column=1)

# print values
value_button = Button(root, text='Print values', width=10, command=print_item_values)
value_button.grid(row=0, column=1)

root.mainloop()
