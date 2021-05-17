from tkinter import *
from center import *

root = Tk()
root.title("Demo window")
centerwin(root, 500, 400)

lbl = Label(root, text = "Hello There!!").pack()

root.mainloop()