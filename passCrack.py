#! /usr/local/bin/python
# passCrack.py
# Given a list of m sets of n sweetwords, identify the real password
# Luke Ahn | Jennifer Ding | Sarah Le Cam | Joe Bassam Abi Sleiman
import sys
import numpy as np
import sklearn.cluster
import distance
from random import shuffle
import string
import enchant

def strip_frequencies_first_18661(filename):
    tr_list = [ ]

    if sys.version_info[0] == 3:
        lines = open(filename,"r",errors='ignore').readlines()
    else:
        lines = open(filename,"r").readlines()
    tr_list = [line.rstrip('\n') for line in lines[:18661]]
    tr_list = [line.split()[1] if len(line.split()) > 1 else line.split()[0] for line in tr_list]
    return tr_list


def isInDictionary(password):
    dictionary = strip_frequencies_first_18661("rockyou-withcount.txt")
    # print(len(dictionary))
    for entry in dictionary:
        if password == entry:
            return True
    return False

def calculate_entropy(input):
    d = enchant.Dict("en_US")
    score = 0
    specialChars = string.punctuation

    if isInDictionary(input):
        score += 10

    # if only numbers, check if sequence or repetitive and add 20 points to score
    if input.isdigit():
        if input == len(input) * input[0] or input in "0123456789876543210":
            score += 20
        else:
            score += 11

    # if the password is made up entirely of characters
    elif len([c for c in input if c.isalpha()]) == len(input):
        score += 5
        # print (type(str(input))
        if (d.check(str(input))):
            # print (input)
            score += 20
    else :
        score += 5
        if (input[0].isalpha() and input[-1].isdigit()):
            score += 10

    # if password has more than 50 percent special characters, increase ration to 1.5
    if len([c for c in input if c in specialChars]) >= len(input)*0.3:
        score -= 30

    capitalizationChanges = 0
    for idx,val in enumerate(input[0:-1]):
        if input[idx].isalpha() and input[idx+1].isalpha():
            if input[idx].islower() != input[idx+1].islower():
                capitalizationChanges += 1
        elif input[idx].isalpha() and input[idx+1].isdigit():
            capitalizationChanges += 1
        elif input[idx].isdigit() and input[idx+1].isalpha():
            capitalizationChanges += 1
    if capitalizationChanges>3:
        score -=15
    elif capitalizationChanges>1:
        score -=5
    print(input,"score",score)
    return score

def choose_pass(password_list):
    max_index = 0
    max_score = 0
    for index, password in enumerate(password_list):
        current_score = calculate_entropy(password)
        if current_score > max_score:
            max_score = current_score
            max_index = index
    return password_list[max_index]

# print (isInDictionary("123456"))

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
        pw_list.append(line.strip("\n") )

    return pw_list

# Write password choice index to output file
def write_passwordchoice_file(filename, password_list):
    # Open file (different based on Python version) in write mode
    if sys.version_info[0] == 3:
        file = open(filename,"w",errors='ignore')
    else:
        file = open(filename,"w")

    output = ", ".join(password_list)
    file.write(output)
    file.close()

def cluster(sweetwords_list, n):

    sweetwords_dist = np.zeros(n)
    sweetwords_list = np.asarray(sweetwords_list)
    similarity = -1*np.array([[distance.levenshtein(w1,w2) for w1 in sweetwords_list[0]] for w2 in sweetwords_list[0]])

    affprop = sklearn.cluster.AffinityPropagation(affinity="precomputed", damping=0.5)
    affprop.fit(similarity)
    roots = dict()

    for cluster_id in np.unique(affprop.labels_):

        exemplar = sweetwords_list[0][affprop.cluster_centers_indices_[cluster_id]]
        cluster = np.unique(sweetwords_list[0][np.nonzero(affprop.labels_==cluster_id)])
        cluster_str = ", ".join(cluster)
        # print(" - *%s:* %s" % (exemplar, cluster_str))

        roots.setdefault(exemplar, [])

        for child in cluster:
            roots[exemplar].append(child)
    return roots

def entropy(roots_dict):
    roots=[]
    for k, v in roots_dict.items():
        roots.append(k)
    entropy=np.ones(len(roots))

    for ind, sweetword in enumerate(roots):
        for char in sweetword:
            if char.isalpha():
                entropy[ind] = entropy[ind]*26
                # entropy[ind] += (1/26) * np.log(1/26)
            elif char.isdigit():
                entropy[ind] = entropy[ind]*10
                # entropy[ind] += (1/10) * np.log(1/10)
            elif set('[~!@#$%^&*()_+":;\]+$').intersection(char):
                entropy[ind] = entropy[ind]*20
                # entropy[ind] += (1/20) * np.log(1/20)
        # entropy[ind] = -1*entropy[ind]

    min_entropy = np.where(entropy == min(entropy))
    min_entropy_roots = []
    for en in min_entropy[0]:
        min_entropy_roots.append(roots[en])

    return min_entropy_roots

def passSelect(roots_dict):

    #delete roots with only one child
    onecount=[]
    for k, v in roots_dict.items():
        if len(v) == 1:
            onecount.append(k)

    for k in onecount:
        roots_dict.pop(k, None)

    #identify min entropy passwords
    highentropy=[]
    min_entropy_roots = entropy(roots_dict)
    for k, v in roots_dict.items():
        if k not in min_entropy_roots:
            highentropy.append(k)

    for k in highentropy:
        roots_dict.pop(k, None)

    #choose root with most children from min entropy list
    maxcount = max(len(v) for v in roots_dict.values())
    return [k for k, v in roots_dict.items() if len(v) == maxcount]

# Define runtime call
def main():
	# get command line aguments
    args = sys.argv

    # m - # of sets of sweetwords
    # n - # of sweetwords in each set
    m = int(args[1])
    n = int(args[2])
    input_file = args[3]

	# store input passwords
    password_list = []
    sweetwords = read_password_file(input_file)

    filename = "password_choice.txt"
	# Identify password for each set of sweetwords

    for row in range(0,m):

        sweetwords_list = []
        sep = ','
        sweetwords_list.append(sweetwords[row].split(sep,n))
        roots = cluster(sweetwords_list, n)
        root_list = []

        for key,val in roots.items():
            # print(key,val)
            length = len(val)
            root_list.append([key,length])

            # root_list.append(key)
        root_list=sorted(root_list,key=lambda x: x[1])

        root_list_processed =[]
        # print(root_list)
        if len(root_list) > 5:
            root_list_processed = [root_list[0][0],root_list[1][0],root_list[-1][0],root_list[-2][0]]
        else:
            for item in root_list:
                root_list_processed.append(item[0])
        print(root_list_processed)
        shuffle(root_list_processed)
        chosen = choose_pass(root_list_processed)
        print("Final Answer", chosen)

        # password_choice = "".join(str(x) for x in passSelect(roots)[0])
        # print("Password Guess #",row, ": ", password_choice)

        password_choice_ind = sweetwords_list[0].index(chosen)
        password_list.append(str(password_choice_ind))

    write_passwordchoice_file(filename, password_list)

# Principal function call
main()
