from Tkinter import *

from model.enigmpy import *
from view.enigmpy_view import *



enigma=EnigmPy()
enigmpy_view = enigmpy_view(enigma)
enigmpy_view.draw()