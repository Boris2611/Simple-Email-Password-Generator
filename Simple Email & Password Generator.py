import random

file = open("output.txt", "w+")

generating = int(input("Number of Emails & Passwords: "))

for i in range(generating):
    file.write("{0:10}".format(str(i + 1) + ") "))
    
    letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
                "a", "s", "d", "f", "g", "h", "j", "k", "l", "z",
                "x", "c", "v", "b", "n", "m"]

    passwordLong = []
    for i in range(25):
        passwordLong.append(letters[i])
        passwordLong.append(letters[i].upper())
    for i in range(10):
        passwordLong.append(str(i))

    passwordLenght = random.randint(8,15)
    random.shuffle(passwordLong)


    emailLong = []
    for i in range(25):
        emailLong.append(letters[i])
    for i in range(10):
        emailLong.append(str(i))

    emailLenght = random.randint(7, 15)
    random.shuffle(emailLong)

    file.write("Email:  ")
    email = ""
    
    for i in range(emailLenght):
        email += emailLong[i]
    email += "@"

    emailExtension = ["gmail", "yahoo", "outlook", "hotmail", "yandex.mail"]
    

    email += emailExtension[random.randint(0, 4)]
    

    email += ".com"
    
    file.write("{0:35}".format(email))

    


    


    file.write("Password:  ")
    for i in range(passwordLenght):
        file.write(passwordLong[i])

    file.write("\n")
    







file.close()
exit()
