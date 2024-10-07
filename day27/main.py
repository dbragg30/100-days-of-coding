from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI Program")
window.wm_minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid()
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)
    # my_label["text"] = "New Text"

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

# button
button = Button(text="click me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)
# Entry

new_button = Button(text="click me too", command=button_clicked)
new_button.grid(column=2, row=0)

input = Entry(width=10)
#input.pack()
input.grid(column=3, row=3)


window.mainloop()


