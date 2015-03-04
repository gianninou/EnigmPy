class Reflector(object):

	def __init__(self,reflector):
		self.reflector=reflector


	def io(self,numb):
		return self.reflector[numb]

	def oi(self,numb):
		return self.reflector.index(numb)
