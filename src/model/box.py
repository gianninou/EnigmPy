from model.rotor import *
from model.plugboard import *
from model.reflector import *

#
#	This class is a box with part of Enigma machine
#	You can choose original rotor, Reflector and plugboard
#	Or create yourself
#

class Box(object):


	############################################
	####               ROTORS               ####
	############################################

	#########
	# rotors I II III : enigma I 1933 (wikipedia)
	#########

	def getRotorI(turnover=17,position=0):
		return Rotor([4,10,12,5,11,6,3,16,21,25,13,19,14,22,24,7,23,20,18,15,0,8,1,17,2,9],turnover,position)
	getRotorI=staticmethod(getRotorI)


	def getRotorII(turnover=5,position=0):
		return Rotor([0,9,3,10,18,8,17,20,23,1,11,7,22,19,12,2,16,6,25,13,15,24,5,21,14,4],turnover,position)
	getRotorII=staticmethod(getRotorII)

	def  getRotorIII(turnover=22,position=0):
		return Rotor([1,3,5,7,9,11,2,15,17,19,23,21,25,13,24,4,8,22,6,0,10,12,20,18,16,14],turnover,position)
	getRotorIII=staticmethod(getRotorIII)

	#########
	# rotors IV V : M3 Army (wikipedia)
	#########

	def getRotorIV(turnover=10,position=0):
		return Rotor([4,18,14,21,15,25,9,0,24,16,20,8,17,7,23,11,13,5,19,6,10,3,2,12,22,1],turnover,position)
	getRotorIV=staticmethod(getRotorIV)
	
	def getRotorV(turnover=0,position=0):
		return Rotor([21,25,1,17,6,8,19,24,20,15,18,3,13,7,11,23,0,22,12,9,16,14,5,4,2,10],turnover,position)
	getRotorV=staticmethod(getRotorV)


	############################################
	####              PlugBoard             ####
	############################################

	def getPlugboard():
		return Plugboard([2,1,0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
	getPlugboard=staticmethod(getPlugboard)


	############################################
	####              Reflector             ####
	############################################

	def getReflectorA():
		return Reflector([4,9,12,25,0,11,24,23,21,1,22,5,2,17,16,20,14,13,19,18,15,8,10,7,6,3])
	getReflectorA=staticmethod(getReflectorA)