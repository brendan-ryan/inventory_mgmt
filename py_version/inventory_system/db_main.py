from tkinter import *
from tkinter import ttk
import sqlite3
from buttons.show_inventory import *

window = tk.Tk()

btn_frame = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)
btn_frame.pack()

print_inv_btn = tk.Button(
    text="Display Inventory Products",
    master=btn_frame,
    width=100,
    height=5
)
print_inv_btn.pack()


print_inv_btn.bind("<Button-1>", handle_print_inv_click)

window.mainloop()