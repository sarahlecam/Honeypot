#! /usr/local/bin/python
# passCrack.py
# Given a list of m sets of n sweetwords, identify the real password
# Luke Ahn | Jennifer Ding | Sarah Le Cam | Joe Bassam Abi Sleiman
import sys
import numpy as np
import sklearn.cluster
import distance

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
        print(" - *%s:* %s" % (exemplar, cluster_str))
        roots[exemplar] = cluster_str

    return roots

def passSelect(roots_dict):

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
        password_choice = "".join(str(x) for x in passSelect(roots))
        print("Password #",row, ": ", password_choice)
        password_choice_ind = sweetwords_list[0].index(password_choice)
        password_list.append(str(password_choice_ind))

    write_passwordchoice_file(filename, password_list)

# Principal function call
main()
