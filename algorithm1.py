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

	#please help this Sarah
	# if checkYear(password)==True:
	# 	temp = n//4
	# 	n = n-temp
	# 	while temp>0:
	# 		res.append(changeYear(password))
	# 		temp = temp-1
	# print (n)
	# get valid heuristic options and their probabilities
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

def checkYear (password):
	tokenizedPW = re.split('(\d+)',password)

	for ind,val in enumerate(tokenizedPW):
		if len(val)>0 and val[0].isdigit():
			if (int(val)>1930) and (int(val) < 2100):
				return True
	return False

def changeYear(password):

	tokenizedPW = re.split('(\d+)',password)

	for ind,val in enumerate(tokenizedPW):
		if len(val)>0 and val[0].isdigit():
			if (int(val)>1930) and (int(val) < 2100):
				newYear = int(val) + random.randint(-30,30)
				tokenizedPW[ind] = str(newYear)
	
	output = ''.join(tokenizedPW)
	return output

	# yyyy = 1
	# yearEnd=0
	# for i in range(1,len(pw_item_Array)):
	# 	if pw_item_Array[i].isdigit() and pw_item_Array[i-1].isdigit():
	# 		yyyy = yyyy+1
	# 	if yyyy == 4:
	# 		yearEnd = i
	# 		print('year found');

	# if yearEnd==len(pw_item_Array)-1:
	# 	first = password[:yearEnd-3]
	# 	second = password[yearEnd-3:]
		
	# 	if int(second)>1930 and int(second)<2100:
	# 		second = int(second)

		
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

