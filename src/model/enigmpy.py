from rotor import *
from plugboard import *
from reflector import *
from box import *

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
