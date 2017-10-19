# CS 5435 HW3
# Given real passwords P, generate "n" sweetwords
# Create 3 Algorithms for the following training sets
#   1) No training
#   2) 100 most common Rock You passwords
#   3) Full Rock You password dataset
import random

# Change all digits to a random number in password

for i, line in enumerate(open('rockyou-withcount.txt')):
        password = line.strip().split()[1]
        if i<100:
            password_new = list(password)
            for j, c in enumerate(password_new):
                if c.isdigit():
                    rand_digit = random.randint(0,9)
                    password_new[j] = str(rand_digit)
                password_final = "".join(password_new)
            dig_check = len([c for c in password if c.isdigit()])
            if dig_check > 0:
                print(password, password_final)
        else:
            break
# Add 3-digit tail if password only has characters

# for i, line in enumerate(open('rockyou-withcount.txt')):
#         password = line.strip().split()[1]
#         if i<100:
#             dig_check = len([c for c in password if c.isdigit()])
#             if dig_check == 0:
#                 rand_digit = str(random.randint(100,999))
#                 password_final = password + rand_digit
#                 print(password, password_final)
#         else:
#             break


# Read first 100 passwords
# for i, line in enumerate(open('rockyou-withcount.txt')):
#         password = line.strip().split()[1]
#         if i<100:
#             dig_check = len([c for c in password if c.isdigit()])
#             print(i+1, password, dig_check)
#         else:
#             break
