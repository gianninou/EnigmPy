from EnigmPy import EnigmPy

enigma = EnigmPy()

print "Welcome to the EnigmPy Machine"
choise = raw_input("1 : Encryption\n2 : decryption\n")

if choise=="1":
	text = raw_input("Enter your plaintext :\n")
	ciphertext = enigma.crypt(text)
	print "The ciphertext is : "+ciphertext

elif choise=="2":
	text = raw_input("Enter your ciphertext :\n")
	plaintext = enigma.crypt(text)
	print "The plaintext is : "+plaintext

else:
	print "Choose the good choice !"
