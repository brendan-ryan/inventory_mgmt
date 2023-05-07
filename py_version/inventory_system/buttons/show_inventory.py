from tkinter import *
from tkinter import ttk
import sqlite3


class Table:
    def __init__(self, root):
        root.title("Current Inventory")

        inv_window = ttk.Frame(root)
        inv_window.grid(column=0, row=0, sticky=(N, S, E, W))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        current_inventory = self.get_inventory()
        conn = sqlite3.connect("StoreDB")
        c = conn.cursor()
        current_inventory = c.execute("SELECT \
            idProduct, \
            Name, \
            Price, \
            CategoryID, \
            Description \
            FROM Product;")
        col_num = 0
        row_num = 0
        for val in current_inventory:
            while col_num < 5:
                self.e = ttk.Entry(inv_window)
                self.e.grid(row=row_num, column=col_num)
                self.e.insert(END, val)
                col_num = col_num + 1
                row_num = row_num + 1


        conn.commit()
        conn.close()


