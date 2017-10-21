#! /usr/local/bin/python
# algorithm1.py
# Given a list of k real passwords, generate k lists of "n" sweetwords with no training data
# Luke Ahn | Jennifer Ding | Sarah Le Cam | Joe Bassam Abi Sleiman

# External Libraries
import random
import sys
import string

# weights helps determine the frequency with which each transform function should be called
#	- Option 0: Manipulate last 3 digits
#	- Option 1:
#	- Option 2:

# TODO: define options
# TODO: change weigths
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


## OPTION 0
# TODO: Check
def manipulate_last_3_char(pw_item):
    """ print n passwords and return list of them """
    sumValues = pw_item.lower().count('s') + pw_item.lower().count('o') + pw_item.lower().count('i') + pw_item.lower().count('a')
    pw_item_Array = list(pw_item)
    for idx,val in enumerate(pw_item_Array):
        if len(pw_item_Array)>3:
            if pw_item_Array[-1].isalpha()== True:
                pw_item_Array[-1] = random.choice(string.ascii_letters)
            else:
                pw_item_Array[-1] = str(random.randint(0,9))


            if pw_item_Array[-2].isalpha()== True:
                pw_item_Array[-2] = random.choice(string.ascii_letters)
            else:
                pw_item_Array[-2] = str(random.randint(0,9))

            if pw_item_Array[-3].isalpha()== True:
                pw_item_Array[-3] = random.choice(string.ascii_letters)
            else:
                pw_item_Array[-3] = str(random.randint(0,9))

        output = ''.join(pw_item_Array)
    return output


## OPTION 1
# TODO: working?   
# Change all digits to a random number in password
def changeAlldigits(password) :
    password_new = list(password)
    for j, c in enumerate(password_new):
        if c.isdigit():
            rand_digit = random.randint(0,9)
            password_new[j] = str(rand_digit)
        password_final = "".join(password_new)
    dig_check = len([c for c in password if c.isdigit()])
    if dig_check > 0:
        # print(password, password_final)
    return password_final


# Find function options
def findOptions() :
	# TODO: determine valid options
	options = list(range(3))
	return options


# Determine probability of each function being applied
def findProbabilities(options) :
	# TODO: change for customized weights
	optweigths = weights
	totalWeights = sum(optweigths)

	# compute probability of each heuristic application
	probabilities = []
	for option in options :
		probability = weights[option]/totalWeights
		probabilities.append(probability)

	return probabilities


# choose option from the available ones
def pickOption(options, probabilities) :
	# Use random float to determine sweetword generation function
	random0to1 = random.random()
	if (random0to1 < probabilities[0]) :
		option = options[0]
	elif (random0to1 < sum(probabilities[0:2])) :
		option = options[1]
	else :
		option = options[2]

	return option


# Find n-1 sweetwords 
def makeSweet(password, option) :
	# switch heuristic transform based on option
	if (option == 0) :
		newPassword = manipulate_last_3_char(password)
	elif (option == 1) :
		newPassword = changeAlldigits(password)
	elif (option == 2) :
		newPassword = "cool"
	return newPassword
 

# Compile sweetwords for given password
def compileSweets(n, password) :
	# get password stats: length, number of digits, number of letters, number of special characters
	stats = getPassStats(password)

	# get valid heuristic options and their probabilities
	options = findOptions()
	probabilities = findProbabilities(options)


	# make the list sweetwords
	sweetwords = [password]
	for i in range(n) :
		# Find a valid heuristic option
		option = pickOption(options, probabilities)
		# generate sweetword
		sweetword = makeSweet(password, option)
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

