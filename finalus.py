Master = input("ENTER MASTER PASSWORD:\n")
import random
import pyperclip
if Master == "monalisa2020":
#if Master == "1":
    option = "0"

    while option != "4":
        print("-------------------")
        print("1: Search password")
        print("2: Add new password")
        print("3: Generate Password")
        print("4: Quit")
        option = input("Choose an option: ")
        print(" ")

        if option == "1":
            found = 0
            f = open("list.txt", "r")
            listOfLines = f.readlines()
            while found == 0:
                counter=-1
                choice = input("Enter website name: ")
                choice = choice.lower()
                for line in listOfLines:
                    counter = counter+1
                 
                    if ("site:"+choice+".com") in line:
                        print("_____________________")
                        print(" ")
                        print("Username: ", end = '')
                        print(listOfLines[(counter+1)])
                        usernamecopy = listOfLines[(counter+1)]
                        print("Password: ", end = '')
                        print(listOfLines[(counter+2)])
                        passwordcopy = listOfLines[(counter+2)]
                        print("_____________________")
                        

                        copychoice = 0
                        while copychoice != 3:
                            print(" ")
                            print("1: Copy Username")
                            print("2: Copy Password")
                            print("3: Back to Main Menu")
                        
                            copychoice = int(input("Pick an option: "))
                            if copychoice == 1:
                                pyperclip.copy(usernamecopy)
                                print("Username copied to clipboard")
                            if copychoice == 2:
                                pyperclip.copy(passwordcopy)
                                print("Password copied to clipboard")
                        
                        found = 1

        if option == "2":
            save = 0
            f = open("list.txt", "a")
            site = input("Enter the name of the site:")
            print(" ")
            site = site.lower()
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            print(" ")

            print("1: SAVE")
            print("2: CANCEL ")
            save = int(input("Choose an option: "))

            if save == 1:
                f.write("\n")
                f.write("\n")
                f.write("site:"+site+".com")
                f.write("\n")
                f.write(username)
                f.write("\n")
                f.write(password)

        if option == "3":
            f = open("list.txt", "r")

            symbol = 0
            lower = 0
            upper = 0
            number = 0
            count = 0
            password = []

            length = input("How many characters should the password be?\n")
            length = 128 if length is '' else int(length)

            #randomly select ascii character classes and individual characters

            while count < length:
                rand = random.randint (0,3)
                if rand == 0:
                    lower += 1
                    b = int(random.randint (97,123))
                    password.append(b)
                elif rand == 1:
                    upper += 1
                    b = random.randint (65,91)
                    password.append(b)
                elif rand == 2:
                    number += 1
                    b = random.randint (48,58)
                    password.append(b)
                elif rand == 3:
                    r = random.randint(0,2)
                    symbol += 1
                    if r == 0:
                        b = random.randint (33,48)
                        password.append(b)
                    elif r == 1:
                        b = random.randint (91,97)
                        password.append(b)
                    elif r == 2:
                        b = random.randint (123,126)
                        password.append(b)
                count += 1

            #convert ascii code to characters
            word = "".join([chr(c) for c in password])

            #copy pass to clipboard
            pyperclip.copy(word)

            #print the result
            print ("Random password of length %s is: \n" % length)

            print('-------------------')
            print(" ")
            print(word)
            print(" ")
            print('-------------------')

            
            print ("The password is copied to your clipboard")



        f.close()
