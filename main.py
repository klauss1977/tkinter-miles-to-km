from tkinter import *


def button_clicked():
    new_text = user_input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

my_label = Label(text="New text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

my_button = Button(text="Click me!", command=button_clicked)
my_button.grid(column=1, row=1)

user_input = Entry()
user_input.grid(column=3, row=3)

my_new_button = Button(text="New button")
my_new_button.grid(column=2, row=0)

window.mainloop()
