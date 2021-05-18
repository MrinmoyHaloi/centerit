from tkinter import *
from centerit import *

root = Tk()
root.title("Demo window")
centertk(root, 500, 400)

lbl = Label(root, text = "Hello There!!").pack()

root.mainloop()