# External Libraries
import random
import sys
import string
import re
import operator

def read_password_file(filename):
    pw_list = [ ]

    # Read file (different based on Python version) and store contents in lines []
    if sys.version_info[0] == 3:
        lines = open(filename,"r",errors='ignore').readlines()
    else:
        lines = open(filename,"r").readlines()

    # add each truncated element of lines to password list
    for line in lines:
        pw_list.extend( line.split() )

    return pw_list

def getPassStats(password) :
	# String -> List
	passChars = list(password)
	length = len(passChars)

	# find makeup of password
	nLetters = 0
	nDigits = 0
	nSpecial = 0
	for i in range(length):
		if (passChars[i] in string.ascii_letters):
			nLetters += 1
		elif (passChars[i] in string.digits):
			nDigits += 1
		else :
			nSpecial += 1

	if nLetters > nDigits and nLetters > nSpecial:
		maxchar = "nLetters"
	elif nDigits > nLetters and nDigits > nSpecial:
		maxchar = "nDigits"
	else:
		maxchar = "nSpecial"

	return {"length": length, "nLetters": nLetters,
				"nDigits": nDigits, "nSpecial": nSpecial, "maxChar": maxchar}




#number - number of honeywords needed
def buildPassList(number, inputpassword):

	passlist = []
	posspass = []

	#For "RockYou Like" passwords
	for i, line in enumerate(open('rockyou-withcount.txt')):
		if i<2000:
			password = line.strip().split()[1]
			if getPassStats(password)["length"] == getPassStats(inputpassword)["length"] and getPassStats(password)["maxChar"] == getPassStats(inputpassword)["maxChar"]:
				posspass.append(password)

		else:
			break

	if(len(posspass) > 0):
		dif = number - len(passlist)
		while (dif > 0) :
			randPass = random.choice(posspass)
			if (randPass not in passlist) :
				passlist.append(randPass)
				dif -= 1

	#For non "RockYou Like" Passowrds
	if (len(passlist) < number) :
		top100rocku = read_password_file("Rocku/rockutop100.csv")
		dif = number - len(passlist)
		while (dif > 0) :
			randPass = random.choice(top100rocku)
			if (randPass not in passlist) :
				passlist.append(randPass)
				dif -= 1

	print(passlist)


realpass = "jwoeirwoieirjowreiowrowru"
buildPassList(10, realpass)
