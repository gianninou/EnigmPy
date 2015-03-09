from model.enigmpy import *

enigma = EnigmPy()

print ("Welcome to the EnigmPy Machine")
choice = input("1 : Encryption\n2 : Decryption\n")

if choice=="1":
	text = input("Enter your plaintext :\n")
	ciphertext = enigma.crypt(text)
	print ("The ciphertext is : "+ciphertext)

elif choice=="2":
	text = input("Enter your ciphertext :\n")
	plaintext = enigma.crypt(text)
	print ("The plaintext is : "+plaintext)

else:
	print ("Choose the good choice !")
