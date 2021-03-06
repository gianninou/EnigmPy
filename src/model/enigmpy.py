from model.rotor import *
from model.plugboard import *
from model.reflector import *
from model.box import *

class EnigmPy(object):
	
	def __init__(self):
		#def rotors
		rotor1 = Box.getRotorI()
		rotor1.position=21
		rotor2 = Box.getRotorIII()
		rotor1.position=21
		rotor3 = Box.getRotorIII()
		rotor1.position=9
		self.rotors=[rotor1,rotor2,rotor3]
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
			cl=self.get_courant(c,all=False)
			#append encoder letter 
			crypt+=chr(cl+ord('a'))
		return crypt

	def get_courant(self,letter,all=False):
		res=[]
		c=ord(letter)-ord('a')
		res.append(ord(letter)-ord('a'))
		c=self.plugboard.io(c)
		res.append(c)
		for r in self.rotors:
			c=r.io(c)
			res.append(c)
		c=self.reflector.io(c)
		res.append(c)
		for r in reversed(self.rotors):
			c=r.oi(c)
			res.append(c)
		c=self.plugboard.oi(c)
		res.append(c)

		if all:
			return res
		else:
			return res[-1]
			
		return crypt

	def reset(self):
		for r in self.rotors:
			r.reset()
