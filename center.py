# I will use win32api library for getting the screen dimensions
#please install pywin32
try:
	from win32.win32api import GetSystemMetrics
except ImportError:
	print("Required libraries not install")

def xpos(width):
    xposi = GetSystemMetrics(0)/2 - width/2
    return xposi

def ypos(height):
    yposi = GetSystemMetrics(1)/2 - height/2
    return yposi

def centerwin(win, width, height):
    win.geometry(f'{width}x{height}+{int(xpos(width))}+{int(ypos(height))}')