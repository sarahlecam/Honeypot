import string
import random

passChars = []
length = 0
nDigits = 0
nLetters = 0
nSpecial = 0

def syntax(p):
	global passChars, length, nDigits, nLetters, nSpecial
	passChars = list(p)
	# print (passChars)
	length = len(passChars)
	# print (length)
	for i in range(length):
		# print (i)
		if (passChars[i] in string.ascii_letters):
			nLetters += 1
		elif (passChars[i] in string.digits):
			nDigits += 1
		else :
			nSpecial += 1
	# return passChars

def capFirst(p) :
	if (passChars[0].isupper()) :
			passChars[0] = passChars[0].lower()
	else :
		passChars[0] = passChars[0].upper()
	return ''.join(passChars)

def capRandom(p):
	cont = 1
	while (cont == 1) :
		i = random.randrange(length)
		if (passChars[i].isupper()) :
			passChars[i] = passChars[i].lower()
		else :
			passChars[i] = passChars[i].upper()
		cont =  random.randrange(2);
		# print (cont)
	return ''.join(passChars)

def randPass() :
	for i in range(length):
		passChars[i] = random.choice(string.ascii_letters + string.digits)
	return ''.join(passChars)

password = "heywhat'sup"
syntax(password)
print (capRandom(password))



