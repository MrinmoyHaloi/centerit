![Build 0.2](https://img.shields.io/badge/Build-0.2-brightgreen) ![Python 3.9.5](https://img.shields.io/badge/Python-3.9.5-green)
# center_it
## A python library for centering the tkinter and PyQt windows.
You can use this library to center your Tkinter or PyQt windows on both x and y cordinates.
### How to use

First clone the repository using 
```bash
git clone https://github.com/MrinmoyHaloi/center_it
```
or [download](https://github.com/MrinmoyHaloi/center_it/archive/refs/heads/main.zip) as a zip file and extract it.
Then import everything from the library using

`from centerit import *`

Then Call centertk for Tkinter
```python
centertk(root, width, height)
``` 
and centerqt for PyQt5
```python
centerqt(root, width, height)
``` 
You just have to pass the root window name and the dimensions you want for your root window.

I used python 3.9.5 to develop it. I didn't test it with other versions of python. I will apreciate if someone test it out with other versions. I will try to add support for other gui libraries in the future. Like wxPython, PyQt4, PySide2 etc.
