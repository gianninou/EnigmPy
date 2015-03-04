from plugboard_view import *
from reflector_view import *
from rotor_view import *

from Tkinter import *

class enigmpy_view(object):

	def __init__(self,enigmpy):
		self.enigmpy=enigmpy
		self.tk=Tk()
		self.canvas=Canvas(self.tk,bg='white',height=700,width=1000)
		self.canvas.pack(side=LEFT)
		bou1 = Button(self.tk,text='Quitter',command=self.tk.quit)
		bou1.pack()

		self.plugboard_view = plugboard_view(enigmpy.plugboard)
		self.reflector_view = reflector_view(enigmpy.reflector)
		
		self.rotors_view=[]
		for r in enigmpy.rotors:
			self.rotors_view.append(rotor_view(r))

	def draw(self):
		self.plugboard_view.draw(canvas=self.canvas,x0=60,y0=100,width=100,height=500)
		self.rotors_view[0].draw(canvas=self.canvas,x0=210,y0=100,width=100,height=500)
		self.rotors_view[1].draw(canvas=self.canvas,x0=370,y0=100,width=100,height=500)
		self.rotors_view[2].draw(canvas=self.canvas,x0=530,y0=100,width=100,height=500)
		self.reflector_view.draw(canvas=self.canvas,x0=690,y0=100,width=160,height=500)
		self.tk.mainloop() 




