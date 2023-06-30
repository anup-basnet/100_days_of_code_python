# Working with Tkinter

# import tkinter
# window = tkinter.Tk()

from tkinter import *

# window a.k.a screen
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=250)
# Add padding around widgets(input/button/etc)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label.", font=("Arial", 20, "bold"))
# modifying label
my_label["text"] = "new text"
my_label.config(text="another text")
"""
    Three methods to show and place your widgets on the screen.
    But you cannot mix differnt types for same frame, gets error.
    1. pack() 
    2. place(x,y)
    3. grid(column, row)
"""
# my_label.pack()
# my_label.place(x=0, y=100)
my_label.grid(column=0, row=0)


# Button
def button_clicked():
    user_input = input.get()
    print(f"{user_input} got clicked.")
    my_label.config(text=f"{user_input} got clicked.")


button1 = Button(text="Click Me", command=button_clicked)
# button.pack()
button1.grid(column=1, row=1)


button2 = Button(text="Click New Button", command=button_clicked)
# button.pack()
button2.grid(column=2, row=0)


# Entry  --> textbox
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)


window.mainloop()
