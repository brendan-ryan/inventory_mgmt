from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")        # place every widget in a frame to keep themed widgets from clashing with background
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))    # grid places the frame in the root window
root.columnconfigure(0, weight=1)                       # expand to fill extra space if resized 
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)   # Entry widget is a child of mainframe. Configuration options: width and textvariable.
feet_entry.grid(column=2, row=1, sticky=(W, E))                 # Grid places the widget in a certain column and row. Sticky describes how the widget should line up within the grid cell

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# adds padding to every widget (child of mainframe). This is a shortcut to adding padding to each individual widget.
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()                      # automatically puts focus on the Entry widget when the application lauches.
root.bind("<Return>", calculate)        # the Return key also executes the 'calculate' function.

root.mainloop()