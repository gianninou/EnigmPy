from Rotor import *
from Plugboard import *
from Reflector import *
from Box import *

class EnigmPy(object):
	
	def __init__(self):
		#def rotors
		self.rotors=[Box.getRotorI(),Box.getRotorII(),Box.getRotorIII()]
		#def plugboard
		self.plugboard=Box.getPlugboard()
		#def Reflector
		self.reflector=Box.getReflectorA()


	def crypt(self,message):
		crypt=""
		message = message.lower()
		for c in message:
			#rotate rotors
			for r in reversed(self.rotors):
				r.rotate()
				if not r.isTurnover():
					break
			
			#encode letter
			c=self.plugboard.io(ord(c)-ord('a'))
			for r in self.rotors:
				c=r.io(c)
			c=self.reflector.io(c)
			for r in reversed(self.rotors):
				c=r.oi(c)
			c=self.plugboard.oi(c)
			
			#append encoder letter 
			crypt+=chr(c+ord('a'))

			
		return crypt

	def reset(self):
		for r in self.rotors:
			r.reset()
