import tkinter as tk

window = tk.Tk()

frame = tk.Frame(master=window, width=250, height=150)
frame.pack()

label1 = tk.Label(master=frame, text="I'm at (0,0)", bg="red")
label1.place(x=0, y=0)

label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)

window.mainloop()


# Note that if you run this code on a different operating system that uses different font sizes and styles, then the second label might become partially obscured by the window’s edge. That’s why .place() isn’t used often. In addition to this, it has two main drawbacks:

# Layout can be difficult to manage with .place(). This is especially true if your application has lots of widgets.
# Layouts created with .place() aren’t responsive. They don’t change as the window is resized.
