import random

file = open("output.txt", "w+")
names = open("Names.txt", "r")

generating = int(input("Number of Emails & Passwords: "))

letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
                "a", "s", "d", "f", "g", "h", "j", "k", "l", "z",
                "x", "c", "v", "b", "n", "m"]

# Creating Random Name List
namesList = []
for i in range(500):
    name = names.readline()
    
    if ("\n" in name):
        name = name.replace ("\n", "")
    
    namesList.append(name)
            
random.shuffle(namesList)

for i in range(generating):

    
    # Counter
    file.write("{0:10}".format(str(i + 1) + ") "))


    # ---------- EMAIL ----------------
    file.write("Email:  ")
    
    email = ""

    nameIndex = random.randint(0, 499)    

    email += namesList[nameIndex]
    email += str(random.randint(1989, 2021))
    email += "@"
    
    emailEx = ["gmail", "yahoo", "outlook", "hotmail"]
    index = random.randint(0,3)
    email += emailEx[index]
    
    email += ".com"
    
    # Formating Email
    file.write("{0:35}".format(email))
    # ----------------------------------
    


    # ---- Password ---------
    passwordLong = []
    for i in range(25):
        passwordLong.append(letters[i])
        passwordLong.append(letters[i].upper())
    for i in range(10):
        passwordLong.append(str(i))

    passwordLenght = random.randint(8,15)
    random.shuffle(passwordLong)


    file.write("Password:  ")
    for i in range(passwordLenght):
        file.write(passwordLong[i])

    file.write("\n")
    # -----------------------



file.close()
names.close()
exit()
