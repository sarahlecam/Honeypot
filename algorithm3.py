#! /usr/local/bin/python
# algorithm2.py
# Given a list of k real passwords, generate k lists of "n" sweetwords with 100 top passwords
# Luke Ahn | Jennifer Ding | Sarah Le Cam | Joe Bassam Abi Sleiman

# Function file
from transform_functions import *

# Compile sweetwords for given password
def compileSweets(n, password, top100rocku):
	# get password stats: length, number of digits, number of letters, number of special characters
	stats = getPassStats(password)
	res = []

	options = findOptions()
	probabilities = findProbabilities(options)

	# make the list sweetwords
	sweetwords = [password]+res
	

	if n > 10:
		# print("chp1")
		m = n//5
		# print(m)
		remainder = n%5
		# print(remainder)
		fakeRockuList = []


		for j in range(0,m-1):
			# print("chp2")
			sweetword = top100rocku[random.randint(0,99)]
			if sweetword not in fakeRockuList:
				fakeRockuList.append(sweetword)

		# print(fakeRockuList)
		i=0
		#The real password
		while (i < 5):
			# print("chp3")
			# Find a valid heuristic option
			option = pickOption(options, probabilities)

			# generate sweetword
			sweetword = makeSweet(password, option)

			# check if sweetword already in set
			# generate new sweetword if so else add sweetword to set
			if (sweetword not in sweetwords) :
				sweetwords.append(sweetword)
				i += 1


		#fake password
		for k in range(0,m-1):
			fackRockuPW = fakeRockuList.pop()
			i=0
			while (i < 5):
				# Find a valid heuristic option
				option = pickOption(options, probabilities)

				# generate sweetword
				sweetword = makeSweet(fackRockuPW, option)

				# check if sweetword already in set
				# generate new sweetword if so else add sweetword to set
				if (sweetword not in sweetwords) :
					sweetwords.append(sweetword)
					i += 1

		fackRockuPW = fakeRockuList.pop()
		i=0
		while (i < remainder):
			# Find a valid heuristic option
			option = pickOption(options, probabilities)

			# generate sweetword
			sweetword = makeSweet(fackRockuPW, option)

			# check if sweetword already in set
			# generate new sweetword if so else add sweetword to set
			if (sweetword not in sweetwords) :
				sweetwords.append(sweetword)
				i += 1
	else:
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


def compileSweetsFromRocku(n,password,rank,top100rocku):
	# print (n,password,rank)
	sweetwords = [password]

	random.randint(0,n)
	half1 = random.randint(0,n)
	half2 = n-half1
	if rank>half1 and (rank-half2)>half2:
		while (half1>0):
			sweetword = top100rocku[random.randint(0,rank)]
			# print(sweetword)
			if (sweetword not in sweetwords) :
				sweetwords.append(sweetword)
				half1 = half1 - 1

		while (half2>0):
			sweetword = top100rocku[random.randint(rank,99)]
			# print(sweetword)

			if (sweetword not in sweetwords) :
				sweetwords.append(sweetword)
				half2 = half2 - 1
	else:
		while (n>0):
			# print(rank)
			sweetword = top100rocku[random.randint(0,99)]
			# print (sweetword)
			# print (sweetwords)
			if (sweetword not in sweetwords) :
				sweetwords.append(sweetword)
				n = n - 1

	#call function for when n >100!!!!!!!!!!!!!!
	random.shuffle(sweetwords)
	# print("This is it",password,sweetwords)
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
	top100rocku = stripFrequencies2("rockyou-withcount.txt")

	# Compile sweetword sets for each password
	sweetword_lists = []
	for password in passwords:
		inRocku =0
		for i in range(0,100):
			if password == top100rocku[i]:
				inRocku =1
				sweetwords = compileSweetsFromRocku(n, password,i,top100rocku)
		if inRocku ==0:
			sweetwords = compileSweets(n, password,top100rocku)

		sweetword_lists.append(sweetwords)

	# write out sweetword sets to output file
	write_sweetword_file(output_file, sweetword_lists)


# Principal function call
main()

