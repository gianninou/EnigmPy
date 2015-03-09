from view.plugboard_view import *
from view.reflector_view import *
from view.rotor_view import *

from tkinter import *

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

	def draw(self,letter="a",x0=50,y0=50):
		draw_all=False
		gap=10
		state = self.enigmpy.get_courant(letter=letter, all=True)

		self.plugboard_view.draw(canvas=self.canvas,x0=x0,y0=y0,width=100,height=500,input_io=state[0],input_oi=state[8],draw_all=draw_all)
		
		xi=x0+100+gap
		for i in range(len(self.rotors_view)):
			self.rotors_view[i].draw(canvas=self.canvas,x0=xi,y0=y0,width=130,height=500,input_io=state[i+1],input_oi=state[-2-i],draw_all=draw_all)
			xi=xi+130+gap

		self.reflector_view.draw(canvas=self.canvas,x0=xi,y0=y0,width=160,height=500,input=state[4],draw_all=draw_all)
		
	def repaint(self):
		self.canvas.delete("all")
		self.draw()



