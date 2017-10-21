#! /usr/local/bin/python
# algorithm1.py
# Given a list of k real passwords, generate k lists of "n" sweetwords with no training data
# Luke Ahn | Jennifer Ding | Sarah Le Cam | Joe Bassam Abi Sleiman

# External Libraries
import random
import sys
import string

weights = [1,1,1]

# Extract passwords from file
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


# Write to output file
def write_sweetword_file(filename, sweetword_lists):
	# Open file (different based on Python version) in write mode
    if sys.version_info[0] == 3:
        file = open(filename,"w",errors='ignore')
    else:
        file = open(filename,"w")

    for i in range(len(sweetword_lists)) :
    	# transform sweetword set into comma seperated string and write on new line
    	list = sweetword_lists[i]
    	file.write(','.join(list))
    	if (i + 1 < len(sweetword_lists)) :
    		file.write("\n")

    file.close()


# Compile make up statistics of password
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

	return {"length": length, "nLetters": nLetters, 
				"nDigits": nDigits, "nSpecial": nSpecial}


# Find n-1 sweetwords 
def makeSweet(password, stats) :
	global weights

	options = list(range(3))
	print (list)

	# Use random float to determine sweetword generation function
	random0to1 = random.random()

	return password
 

# Compile sweetwords for given password
def compileSweets(n, password) :
	# get password stats: length, number of digits, number of letters, number of special characters
	stats = getPassStats(password)

	# make the list sweetwords
	sweetwords = [password]
	for i in range(n) :
		# generate sweetword
		sweetword = makeSweet(password, stats)
		# check if sweetword already in set
		# generate new sweetword if so else add sweetword to set
		if (sweetword in sweetwords) :
			if (i > 0) :
				i -= 1
		else :
			sweetwords.append(sweetword)

	# randomize order of sweetword set
	random.shuffle(sweetwords)

	return sweetwords


# Define runtime call
def main():
	# get command line aguments
	args = sys.argv
	n = int(args[1]) - 1
	input_file = args[2]
	output_file = args[3]

	# store input passwords
	passwords = read_password_file(input_file)

	# Compile sweetword sets for each password
	sweetword_lists = []
	for password in passwords :
		sweetwords = compileSweets(n, password)
		sweetword_lists.append(sweetwords)

	# write out sweetword sets to output file
	write_sweetword_file(output_file, sweetword_lists)


# Principal function call
main()

