![pypi](https://img.shields.io/pypi/wheel/centerit)
![Python-3.9.2|3.9.3|3.9.4|3.9.5](https://img.shields.io/badge/Python-3.8.5|to|3.9.5-blue) 
![platform win|linux](https://img.shields.io/badge/platform-win%20|%20linux-red)
# centerit
## A python library for centering the tkinter and PyQt windows.
You can use this library to center your Tkinter or PyQt windows both horizontally and vertically. That means your window will show in the middle of the screen.
### How to install

pip install centerit 

or

Clone the repository using 
```bash
git clone https://github.com/MrinmoyHaloi/centerit
```
or [download](https://github.com/MrinmoyHaloi/centerit/archive/refs/heads/main.zip) as a zip file and extract it.

### How to use
import everything from the library using

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

I used python 3.9.5 to develop it. I used windows 10 20H2 and parrot OS 4.11.1 (Debian Based) to test it. I would appreciate if anyone tests it out with other versions of python that is lower than 3.9.2. I will try to add support for other gui libraries in the future, like wxPython, PyQt4, PySide2 etc.

### Thanks to [Cerberus](https://github.com/Cerberus22) for testing in python 3.8.5. 
