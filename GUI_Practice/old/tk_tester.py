import os

os.environ['TK_SILENCE_DEPRECATION'] = '1'

import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
label = tk.Label(
    text="Hello",
    foreground="white",
    background="black",)

label.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="green",
    foreground="yellow",
)

button.pack()

entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()

window.mainloop()
