#! /usr/local/bin/python
# algorithm1.py
# Given a list of k real passwords, generate k lists of "n" sweetwords with no training data
# Luke Ahn | Jennifer Ding | Sarah Le Cam | Joe Bassam Abi Sleiman

# Function file
from transform_functions import *

# Compile sweetwords for given password
def compileSweets(n, password) :
	# get password stats: length, number of digits, number of letters, number of special characters
	stats = getPassStats(password)
	res = []

	options = findOptions()
	probabilities = findProbabilities(options)

	# make the list sweetwords
	sweetwords = [password]+res
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
	for password in passwords:
		inRocku =0
		sweetwords = compileSweets(n, password)
		sweetword_lists.append(sweetwords)

	# write out sweetword sets to output file
	write_sweetword_file(output_file, sweetword_lists)


# Principal function call
main()

