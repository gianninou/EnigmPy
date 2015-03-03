class Plugboard(object):

	def __init__(self,plugboard):
		self.plugboard=plugboard
		

	def io(self,numb):
		return self.plugboard[numb]

	def oi(self,numb):
		return self.plugboard.index(numb)