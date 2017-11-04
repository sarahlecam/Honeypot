#! /usr/local/bin/python
# transform functions
# Luke Ahn | Jennifer Ding | Sarah Le Cam | Joe Bassam Abi Sleiman

# External Libraries
import random
import sys
import string
import re

# weights helps determine the frequency with which each transform function should be called
# TODO: define options
# TODO: change weigths
weights = [1, 1, 1, 1, 1, 3, 1, 1, 1, 2]

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
        # pw = ''.join(line.split("\n")) 
        # print(line.strip("\n"))
        # print(line)
        pw_list.append(line.strip("\n") )
        # print (pw_list)
    return pw_list

def stripFrequencies2(filename):
    tr_list = [ ]

    if sys.version_info[0] == 3:
        lines = open(filename,"r",errors='ignore').readlines()
    else:
        lines = open(filename,"r").readlines()
    tr_list = [line.rstrip('\n') for line in lines]
    tr_list = [line.split()[1] if len(line.split()) > 1 else line.split()[0] for line in tr_list]
    return tr_list

def strip_frequencies_first_18661(filename):
    tr_list = [ ]

    if sys.version_info[0] == 3:
        lines = open(filename,"r",errors='ignore').readlines()
    else:
        lines = open(filename,"r").readlines()
    tr_list = [line.rstrip('\n') for line in lines[:18661]]
    tr_list = [line.split()[1] if len(line.split()) > 1 else line.split()[0] for line in tr_list]
    return tr_list

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
        output = ",".join(list)
        file.write(output)
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

    if nLetters > nDigits and nLetters > nSpecial:
        maxchar = "nLetters"
    elif nDigits > nLetters and nDigits > nSpecial:
        maxchar = "nDigits"
    else:
        maxchar = "nSpecial"

    return {"length": length, "nLetters": nLetters,
                "nDigits": nDigits, "nSpecial": nSpecial, "maxChar": maxchar}


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
    #   if pw_item_Array[i].isdigit() and pw_item_Array[i-1].isdigit():
    #       yyyy = yyyy+1
    #   if yyyy == 4:
    #       yearEnd = i
    #       print('year found');

    # if yearEnd==len(pw_item_Array)-1:
    #   first = password[:yearEnd-3]
    #   second = password[yearEnd-3:]
        
    #   if int(second)>1930 and int(second)<2100:
    #       second = int(second)


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


## OPTION 2
# TODO
#Switching up digit positions
def algo3(passcode):
    password = passcode
    digitIndexes = []

    #looping over password and storing the indexes of digits
    for i in range (len(password)):
        if str.isdigit(password[i]):
            digitIndexes.append(i)

    lst = list(password);

    #loop over the constructed list of indexes and swap them in the original password
    for j in range(int(len(digitIndexes)/2)):
        lst[digitIndexes[j]], lst[digitIndexes[len(digitIndexes)-j-1]] = lst[digitIndexes[len(digitIndexes)-j-1]], lst[digitIndexes[j]]
    
    output = ''.join(lst)
    return (output)


## OPTION 3
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
#please help this Sarah
def diffYear(password) :
    if checkYear(password)==True:
        password = changeYear(password)
    # print (n)
    return password


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
#this assumes that at the very least, the last character is a digit
def algo8(passcode):
    password = passcode
    lst = list(password)
    
    index = len(password)-1
    
    i = ord(lst[index])
    j = ord(lst[index-1])
    
    if(i - j == 1 and i<9):
        temp = i+1
        lst.append(str(i+1))
    elif(j - i == 1 and i>1):
        lst.append(str(i-1))
    elif(i < 9):
        lst.append(str(i+1))
    elif(i == 9):
        lst.append('8')
        
    output = ''.join(lst)
    return (output)


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
    options = list(range(10))
    # print (options)
    return options

## OPTION 9
# TODO
def capFirst(p) :
  passChars = list(p)
  if (passChars[0].isupper()) :
       passChars[0] = passChars[0].lower()
  else :
   passChars[0] = passChars[0].upper()
  return ''.join(passChars)


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
       newPassword = algo3(password)
    elif (option == 3) :
       newPassword = capRandom(password)
    elif (option == 4) :
       newPassword = generate_special_char(password)
    elif (option == 5):
       newPassword = diffYear(password)
    elif (option == 6):
       newPassword = add_tail_or_head(password)
    elif (option == 7):
       newPassword = algo8(password)
    elif (option == 8):
       newPassword = randPass(password)
    elif (option == 9):
       newPassword = capFirst(password) 
    return newPassword

 
