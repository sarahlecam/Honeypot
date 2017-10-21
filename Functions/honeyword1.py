
def generate_special_char( n, pw_list ):
    """ print n passwords and return list of them """
    ans = [ ]
    for pw_item in pw_list:
        sumValues = pw_item.lower().count('s') + pw_item.lower().count('o') + pw_item.lower().count('i') + pw_item.lower().count('a')
        print sumValues;

        pw_item_Array = list(pw_item)
        for idx,val in enumerate(pw_item_Array):

            change_bool = randint(0,1)
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
        print output
    # return ans

def manipulate_last_3_char( n, pw_list ):
    """ print n passwords and return list of them """
    ans = [ ]
    for pw_item in pw_list:
        sumValues = pw_item.lower().count('s') + pw_item.lower().count('o') + pw_item.lower().count('i') + pw_item.lower().count('a')
        print sumValues;

        pw_item_Array = list(pw_item)
        for idx,val in enumerate(pw_item_Array):
            if len(pw_item_Array)>3:

                if pw_item_Array[-1].isalpha()== True:
                    pw_item_Array[-1] = random.choice(string.letters)
                else:
                    pw_item_Array[-1] = str(randint(0,9))


                if pw_item_Array[-2].isalpha()== True:
                    pw_item_Array[-2] = random.choice(string.letters)
                else:
                    pw_item_Array[-2] = str(randint(0,9))

                if pw_item_Array[-3].isalpha()== True:
                    pw_item_Array[-3] = random.choice(string.letters)
                else:
                    pw_item_Array[-3] = str(randint(0,9))

            # if val == 
                # print pw_item_Array
            output = ''.join(pw_item_Array)
        print output
    # return ans

def main():
    # get number of passwords desired
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 20
    # read password files
    filenames = sys.argv[2:]           # skip "gen.py" and n   
    pw_list = read_password_files(filenames)
    # generate passwords
    # new_passwords = generate_special_char(n,pw_list)
    new_passwords = manipulate_last_3_char(n,pw_list)

    # shuffle their order
    # random.shuffle(new_passwords)
    # print if desired
    printing_wanted = True
    # if printing_wanted:
    #     for pw in new_passwords:
    #         print (pw)

# import cProfile
# cProfile.run("main()")

main()
