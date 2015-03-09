from view.part_view import *

class rotor_view(part_view):

	def __init__(self,rotor):
		self.rotor=rotor

	def draw(self,canvas,x0,y0,width,height,input_io=-1,input_oi=-1,draw_all=True):
	    self.draw_box(canvas,x0,y0,width,height)

	    gap=10
	    for l in range(len(self.rotor.rotor)):
	        canvas.create_text(x0+gap,        y0+(l+1)*(height/27),text=chr(((l+self.rotor.position)%26)+ord('a')))
	        canvas.create_text(x0+width-gap,  y0+(l+1)*(height/27),text=chr(((l+self.rotor.position)%26)+ord('a')))
	    
	        width2=1
	        coul='black'
	        if  (l-self. rotor.position)%26 ==input_io or (self.rotor.rotor[l]-self.rotor.position)%26==input_oi:
	            coul='red'
	            width2=2
	        elif not draw_all:
	            continue
	        startx = x0+2*gap 
	        starty = y0+ ((( l -self.rotor.position)%26)+1) *(height/27)

	        endx = x0+width-2*gap
	        endy = y0+(((self.rotor.rotor[l]-self.rotor.position)%26)+1)*(height/27)
	        canvas.create_line(startx,starty,endx,endy,width=width2,fill=coul)