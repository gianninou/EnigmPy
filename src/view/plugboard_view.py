from view.part_view import *

class plugboard_view(part_view):

	def __init__(self,plugboard):
		self.plugboard=plugboard

	def draw(self,canvas,x0,y0,width,height,input_io=-1,input_oi=-1,draw_all=True):
	    self.draw_box(canvas,x0,y0,width,height)

	    gap=10
	    for l in range(len(self.plugboard.plugboard)):
	        canvas.create_text(x0+gap,        y0+(l+1)*(height/27),text=chr(l+ord('a')))
	        canvas.create_text(x0+width-gap,  y0+(l+1)*(height/27),text=chr(l+ord('a')))

	        width2=1
	        coul='black'
	        
	        if l==input_io or self.plugboard.plugboard[l]==input_oi:
	            coul='red'
	            width2=2
	        elif not draw_all:
	            continue

	        startx = x0+2*gap 
	        starty = y0+ (l+1) *(height/27)

	        endx = x0+width-2*gap
	        endy = y0+(self.plugboard.plugboard.index(l)+1)*(height/27)
	        canvas.create_line(startx,starty,endx,endy,width=width2,fill=coul)