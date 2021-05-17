from tkinter import *
from centerit import *

root = Tk()
root.title("Demo window")
centerwin(root, 500, 400)

lbl = Label(root, text = "Hello There!!").pack()

root.mainloop()