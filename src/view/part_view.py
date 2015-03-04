
class part_view(object):

	def __init__():
		pass

	def draw_box(self,canvas,x0,y0,width,height,coul='black'):
		canvas.create_line(x0,        y0,         x0,         y0+height,  width=2,fill=coul)
		canvas.create_line(x0,        y0,         x0+width,   y0,         width=2,fill=coul)
		canvas.create_line(x0+width,  y0+height,  x0,         y0+height,  width=2,fill=coul)
		canvas.create_line(x0+width,  y0+height,  x0+width,   y0,         width=2,fill=coul)
