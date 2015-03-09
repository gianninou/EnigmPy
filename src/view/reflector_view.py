from view.part_view import *

class reflector_view(part_view):

	def __init__(self,reflector):
		self.reflector=reflector

	def draw(self,canvas,x0,y0,width,height,input=-1,draw_all=True):
		self.draw_box(canvas,x0,y0,width,height)

		gap=10
		drawed = set()
		for r in range(len(self.reflector.reflector)):
			canvas.create_text(x0+gap,        y0+(r+1)*(height/27),text=chr(r+ord('a')))
		
			if(r not in drawed and self.reflector.reflector.index(r) not in drawed):
				width2=1
				coul='black'
				if r==input or self.reflector.reflector.index(r)==input:
					coul='red'
					width2=2
				elif not draw_all:
					continue
				drawed.add(r)
				drawed.add(self.reflector.reflector.index(r))

				startx = x0 + 20
				endx = startx + (r+2)+(r*5)
				starty = y0+ (r+1) *(height/27)
				endy = y0+(self.reflector.reflector.index(r)+1)*(height/27)
				canvas.create_line(startx,starty,endx,starty,width=width2,fill=coul)
				canvas.create_line(startx,endy,endx,endy,width=width2,fill=coul)
				canvas.create_line(endx,starty,endx,endy,width=width2,fill=coul)