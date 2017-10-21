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
weights = [1, 1, 1, 1, 1, 1, 1, 1, 1]

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
    # if dig_check > 0:
        # print(password, password_final)
    return password_final


## TODO: get from ipyn == OPTION 2


## OPTION 3
# TODO: merge? Pick one?
def capFirst(p) :
	passChars = list(p)
	if (passChars[0].isupper()) :
			passChars[0] = passChars[0].lower()
	else :
		passChars[0] = passChars[0].upper()
	return ''.join(passChars)

# TODO: check effectiveness of continue (lower bound to <50%)
def capRandom(p):
	passChars = list(p)
	length = len(passChars)
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


## OPTION 4
# TODO
def generate_special_char(pw_item):
    sumValues = pw_item.lower().count('s') + pw_item.lower().count('o') + pw_item.lower().count('i') + pw_item.lower().count('a')
    # print sumValues;

    pw_item_Array = list(pw_item)
    for idx,val in enumerate(pw_item_Array):

        change_bool = random.randint(0,1)
        if change_bool==1:
            if val.lower() == "s":
                pw_item_Array[idx]="$"
            if val.lower() == "o":
                pw_item_Array[idx]="0"
            if val.lower() == "i":
                pw_item_Array[idx]="1"
            if val.lower() == "a":
                pw_item_Array[idx]="@"

        # if val == 
        #     print tArray[idx]
        output = ''.join(pw_item_Array)
    return output

## OPTION 5
# TODO

## OPTION 6
# TODO
# Add 3-digit tail if password only has characters
def add_tail_or_head (password) :
    dig_check = len([c for c in password if c.isdigit()])
    password_final = password
    if dig_check == 0:
    	rand_digit = str(random.randint(100,999))
    	password_final = password + rand_digit
    # print(password, password_final)
    return password_final

## OPTION 7
# TODO: get from ipyn


## OPTION 8
# TODO
def randPass(password) :
	passChars = list(password)
	length = len(passChars)
	for i in range(length):
		passChars[i] = random.choice(string.ascii_letters + string.digits)
	return ''.join(passChars)

# Find function options
def findOptions() :
	# TODO: determine valid options
	options = list(range(9))
	# print (options)
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
	nOpt = len(options)
	if (random0to1 < probabilities[0]) :
			option = options[0]
	for i in range(1, nOpt):
		if (sum(probabilities[0:i]) <= random0to1 < sum(probabilities[0:(i+1)])) :
			option = options[i]

	return option


# Find n-1 sweetwords 
def makeSweet(password, option) :
	# switch heuristic transform based on option
	if (option == 0) :
		newPassword = manipulate_last_3_char(password)
	elif (option == 1) :
		newPassword = changeAlldigits(password)
	elif (option == 2) :
		newPassword = "OPTION 2"
	elif (option == 3) :
		newPassword = capRandom(password)
	elif (option == 4) :
		newPassword = generate_special_char(password)
	elif (option == 5):
		newPassword = "OPTION 5"
	elif (option == 6):
		newPassword = add_tail_or_head(password)
	elif (option == 7):
		newPassword = "OPTION 7"
	elif (option == 8):
		newPassword = randPass(password)
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
	i = 0
	while (i < n) :
		# Find a valid heuristic option
		option = pickOption(options, probabilities)

		# generate sweetword
		sweetword = makeSweet(password, option)

		# check if sweetword already in set
		# generate new sweetword if so else add sweetword to set
		if (sweetword not in sweetwords) :
			sweetwords.append(sweetword)
			i += 1

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

