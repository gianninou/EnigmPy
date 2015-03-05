from Tkinter import *
import time

from model.enigmpy import *
from view.enigmpy_view import *

def task():
	enigma.crypt("a")
	enigmpy_view.repaint()
	enigmpy_view.tk.after(200,task)

enigma=EnigmPy()
enigmpy_view = enigmpy_view(enigma)

enigmpy_view.tk.after(0,task)
enigmpy_view.tk.mainloop()





