from tkinter import *
from tkinter import ttk
from buttons.show_inventory import *

class Bims:
    def __init__(self, root):
        root.title("BIMS - Brendan's Inventory Management System")
        root.geometry('600x300')

        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Button(mainframe, text="Initialize Database", command=self.load_db).grid(column=1, row=1)
        ttk.Button(mainframe, text="Show Current Inventory", command=self.current_inventory).grid(column=1, row=2)
        ttk.Button(mainframe, text="Reports", command=self.reports).grid(column=1, row=3, pady=1)

        spacer = ttk.Separator(mainframe, orient=VERTICAL).grid(column=2, rowspan=5, row=1, padx=5, pady=5, sticky=(N, S))  # keep playing with this

        # notebook section
        n = ttk.Notebook(mainframe)
        n.grid(column=3, row=1)
        add_item = ttk.Frame(n)
        ship_item = ttk.Frame(n)
        receive = ttk.Frame(n)
        n.add(add_item, text="Add New Item")
        n.add(ship_item, text="Ship Items")
        n.add(receive, text="Receive Items")

        # Add new item
        def build_add_item():
            item_name = StringVar()
            name = ttk.Entry(add_item, textvariable=item_name).grid(column=2, row=4)
            name_label = ttk.Label(add_item, text="Item Name").grid(column=1, row=4, sticky=W)

            item_cost = StringVar()
            cost = ttk.Entry(add_item, textvariable=item_cost).grid(column=2, row=5)
            cost_label = ttk.Label(add_item, text="Item Cost").grid(column=1, row=5, sticky=W)

            item_catid = StringVar()
            category_id = ttk.Entry(add_item, textvariable=item_catid).grid(column=2, row=6)
            cat_label = ttk.Label(add_item, text="Category ID").grid(column=1, row=6, sticky=W)

            item_description = StringVar()
            description = ttk.Entry(add_item, textvariable=item_description).grid(column=2, row=7)
            description_label = ttk.Label(add_item, text="Description").grid(column=1, row=7, sticky=W)

            item_quantity = StringVar()
            qty = ttk.Entry(add_item, textvariable=item_description).grid(column=2, row=8)
            qty_label = ttk.Label(add_item, text="Quantity").grid(column=1, row=8, sticky=W)

            ttk.Button(add_item, text="Add New Item", command=ship_item).grid(column=2, row=10)

        # Ship / Receive Items
        def build_ship():
            transaction_type = StringVar()
            ship = ttk.Radiobutton(ship_item, text="Ship", variable=transaction_type, value="Ship").grid(column=1, row=1)
            receive = ttk.Radiobutton(ship_item, text="Receive", variable=transaction_type, value="Receive").grid(column=2, row=1)

            item_name = StringVar()
            name = ttk.Entry(ship_item, textvariable=item_name).grid(column=2, row=4)
            name_label = ttk.Label(ship_item, text="Item Name").grid(column=1, row=4)

            item_cost = StringVar()
            cost = ttk.Entry(ship_item, textvariable=item_cost).grid(column=2, row=5)
            cost_label = ttk.Label(ship_item, text="Item Cost").grid(column=1, row=5)

            item_catid = StringVar()
            category_id = ttk.Entry(ship_item, textvariable=item_catid).grid(column=2, row=6)
            cat_label = ttk.Label(ship_item, text="Category ID").grid(column=1, row=6)

            item_description = StringVar()
            description = ttk.Entry(ship_item, textvariable=item_description).grid(column=2, row=7)
            description_label = ttk.Label(ship_item, text="Description").grid(column=1, row=7)

            item_quantity = StringVar()
            qty = ttk.Entry(ship_item, textvariable=item_description).grid(column=2, row=8)
            qty_label = ttk.Label(ship_item, text="Quantity").grid(column=1, row=8)

            ttk.Button(ship_item, text="Ship Item", command=ship_item).grid(column=2, row=10)

        build_add_item()
        build_ship()    # will this approach work? Might need to unwrap 'build_ship'


    def current_inventory():
        print("You called 'current_inventory' function")
        # root = Tk()
        # Table(root)
        # root.mainloop()

    def load_db():
        pass

    def reports():
        pass

    def ship_item():
        pass


root = Tk()
Bims(root)
root.mainloop()