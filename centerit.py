# Please suggest me new ideas in the github page
# https://github.com/MrinmoyHaloi/center_it

from tkinter import *

try:
	from PyQt5.QtWidgets import *
	import sys
except ImportError:
	print("PyQt5 not installed")

def centertk(win, width, height):
	'''
	You just have to pass the root window name and the dimensions you want for your window.
	'''
	xposi = win.winfo_screenwidth()/2 - width/2
	yposi = win.winfo_screenheight()/2 - height/2

	win.geometry(f'{width}x{height}+{int(xposi)}+{int(yposi)}')

def centerqt(win, width, height):
	'''
	You just have to pass the root window name and the dimensions you want for your window.
	'''
	app = QApplication(sys.argv)
	screen = app.primaryScreen().size()
	xposi = screen.width()/2 - width/2
	yposi = screen.height()/2 - height/2

	win.setGeometry(int(xposi),int(yposi),int(width),int(height))
