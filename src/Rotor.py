class Rotor(object):

	def __init__(self,rotor,turnover=0,position=0):
		self.rotor=rotor
		self.position=position
		self.initposition=position
		self.turnover=turnover


	def io(self,numb):
		return self.rotor[(numb+self.position)%26]

	def oi(self,numb):
		return (self.rotor.index(numb)-self.position)%26

	def rotate(self):
		self.position = (self.position+1)%26

	def isTurnover(self):
		return self.position==self.turnover

	def reset(self):
		self.position=self.initposition
	