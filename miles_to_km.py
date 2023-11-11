from tkinter import *


def button_clicked():
    miles = float(user_input.get())
    km = miles*1.609
    label_1_1.config(text=f"{km}")
    if user_input.get() == "1" or user_input.get() == "0":
        label_2_0.config(text="Mile")
    else:
        label_2_0.config(text="Miles")


window = Tk()
window.title("Miles to Kilometer Converter")
#window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

label_0_1 = Label(text="is equal to: ")
label_0_1.grid(column=0, row=1)
label_0_1.config(padx=50, pady=50)

user_input = Entry(width=7)
user_input.grid(column=1, row=0)
user_input.insert(END, string="0")

label_1_1 = Label(text="0")
label_1_1.grid(column=1, row=1)

label_2_0 = Label(text="Mile(s)")
label_2_0.grid(column=2, row=0)

label_2_1 = Label(text="Km")
label_2_1.grid(column=2, row=1)

my_button = Button(text="Calculate", command=button_clicked)
my_button.grid(column=1, row=2)

window.mainloop()
