from tkinter import *


def calculate():
    miles = round(float(mile_input.get()) * 1.609)
    km_calc.config(text=miles)


# add components to window
window = Tk()

window.wm_minsize(width=500, height=300)
window.config(padx=20, pady=20)
# Title is - Mile to Km Converter
window.title("Miles to Km Converter")

# column1 has label of is equal to at column 1 row 1
eq2_label = Label(text="is equal to")
eq2_label.grid()
eq2_label.grid(column=0, row=1)

# column2 has text box @ grid 2,0 for input
mile_input = Entry(width=10)
mile_input.grid(column=1, row=0)

# column 2 has km output text @grid 2, 1
km_calc = Label(text="0")
km_calc.grid(column=1, row=1)
# column 3 has km calculate button @ grid 2,3
cal_button = Button(text="Calculate", command=calculate)
cal_button.grid(column=1, row=2)

# column 4 has label Miles @ grid 3,0
m_label = Label(text="Miles")
m_label.grid(column=2, row=0)

# column 4 has label Km @ grid 3,1
km_label = Label(text="KM")
km_label.grid(column=2, row=1)

window.mainloop()
