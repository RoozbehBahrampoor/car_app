from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from file_manager import *
from validator import *
from car import Car
car_list = read_from_file("car.dat")


def load_data(car_list):
    car_list = read_from_file("car.dat")
    for row in table.get_children():
        table.delete(row)

    for car in car_list:
        table.insert("", END, values=car)


def reset_form():
    car_id.set(len(car_list) + 1)
    name.set("")
    model.set("")
    color.set("")
    production_date.set("")
    owner.set("")
    load_data(car_list)


def save_btn_click():
    car = (car_id.get(), name.get(), model.get(), color.get(), production_date.get(), owner.get())
    errors = car_validator(car)
    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        msg.showinfo("Saved", "car information saved")
        car_list.append(car)
        write_to_file("car_info.py", car_list)
        reset_form()


def table_select(x):
    selected_car = Car(*table.item(table.focus())["values"])
    if selected_car:
        car_id.set(selected_car.name)
        name.set(selected_car.model)
        model.set(selected_car.color)
        color.set(selected_car.production_date)
        production_date.set(selected_car.owner)



def edit_btn_click():
    pass


def remove_btn_click():
    selected_car = (table.focus())[ "values"]
    if selected_car:
        table.delete(selected_car)


window = Tk()
window.title("car Info")
window.geometry("610x300")

# --- Car ID ---
Label(window, text="Car ID").place(x=20, y=20)
car_id = IntVar(value=1)
Entry(window, textvariable=car_id, state="readonly").place(x=115, y=20)

# --- Name ---
Label(window, text="Name").place(x=20, y=60)
name = StringVar()
Entry(window, textvariable=name).place(x=115, y=60)

# --- Model ---
Label(window, text="Model").place(x=20, y=100)
model = StringVar()
Entry(window, textvariable=model).place(x=115, y=100)

# --- Color ---
Label(window, text="Color").place(x=20, y=140)
color = StringVar()
Entry(window, textvariable=color).place(x=115, y=140)

# --- Production Date ---
Label(window, text="Production_Date").place(x=20, y=180)
production_date = StringVar()
Entry(window, textvariable=production_date).place(x=115, y=180)

# --- Owner ---
Label(window, text="Owner").place(x=20, y=220)
owner = StringVar()
Entry(window, textvariable=owner).place(x=115, y=220)

# --- Table ---
table = ttk.Treeview(window, columns=[1, 2, 3, 4, 5, 6], show="headings")
table.heading(1, text="Car ID")
table.heading(2, text="Name")
table.heading(3, text="Model")
table.heading(4, text="Color")
table.heading(5, text="Production Date")
table.heading(6, text="Owner")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=100)
table.column(6, width=100)


table.bind("<<TreeviewSelect>>", table_select)

table.place(x=260, y=20)

# --- Buttons ---
Button(window, text="Save", width=6, command=save_btn_click).place(x=50, y=290)
Button(window, text="Edit", width=6, command=edit_btn_click).place(x=110, y=290)
Button(window, text="Remove", width=6, command=remove_btn_click).place(x=170, y=290)
Button(window, text="Clear", width=6, command=reset_form).place(x=80, y=250, width=110)

# ---Load initial data ---
reset_form()

window.mainloop()
