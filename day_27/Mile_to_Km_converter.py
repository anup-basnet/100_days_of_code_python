# Project: Miles to Km converter  --- 1 mile = 1.609 kms

from tkinter import *


def calculate_km():
    miles = miles_input.get()
    # print(type(miles))
    km = int(miles) * 1.609
    miles_to_km.config(text=f"{km:.2f}")


# window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=30, pady=30)

# widgets [1 entry and 4 labels and a button]
miles_input = Entry(width=10)
miles_input.focus()
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equla to")
is_equal_label.grid(row=1, column=0)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

miles_to_km = Label(text="0")
miles_to_km.grid(row=1, column=1)


button = Button(text="Calculate", command=calculate_km)
button.grid(row=2, column=1)


window.mainloop()
