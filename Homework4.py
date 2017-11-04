from transform_functions import *

def isInDictionary(password):
    dictionary = strip_frequencies_first_18661("rockyou-withcount.txt")
    print(len(dictionary))
    for entry in dictionary:
        if password == entry:
            return True
    return False

def calculate_entropy(input):
    score = 0
    specialChars = string.punctuation

    if not isInDictionary(input):
        score += 10

    # if only numbers, check if sequence or repetitive and add 20 points to score
    if input.isdigit():
        if input == len(input) * input[0] or input in "0123456789876543210":
            score += 20

    # if the password is made up entirely of characters
    elif len([c for c in input if c.isalpha()]) == len(input):
        score += 10

    else:
        score += 5

    # if password has more than 50 percent special characters, increase ration to 1.5
    if len([c for c in input if c in specialChars]) >= len(input)*0.3:
        score -= 30

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

print (isInDictionary("123456"))