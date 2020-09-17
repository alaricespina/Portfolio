#Password Strengthener
import random

def passwordRandomizer(FName, LName , BMonth = "August", BDate = 28, BYear = 2002):
    inputlist = [FName,LName,BMonth,str(BDate),str(BYear)]
    a, b, c, d, e = " ", " ", " ", " ", " "
    outputlist = [a,b,c,d,e]

    for x in range(0,len(outputlist)-1):
        rstart = random.randint(1,len(inputlist[x])-1)
        rstop = random.randint(1,int(len(inputlist[x])/2))
        for y in range(rstart,rstop):
            outputlist[x] += inputlist[x][rstart:rstop]
        

    return ''.join(outputlist)    



while True:
    print("Password for boomers")
    print("[1] - Create a New Password")
    print("[2] - Store current Password")
    print("[3] - Improve Current Password")
    
    while True:
        mainc = input("Input Number:")

        try: 
            ic = int(mainc)
            break
        except ValueError:
            print("Input a number only please")

    if ic == 1:
        #Create a new Password
        print("The Following information would only be used to create a new password")

        while True:
            filled = True
            FirstName = input("First Name: ")
            LastName = input("Last Name: ")
            BirthMonth = input("Month of Birth: ")
            BirthDate = input("Date of Birth: ")
            BirthYear = input("Year of Birth: ")
            for x in [FirstName,LastName,BirthMonth,BirthDate,BirthYear]:
                if len(x) == 0:
                    filled = False
            if filled == True:
                print("\nInput accepted")
                break
            else:
                print("\nPlease Input Data on Fields")


        #Result from funciton
        while True:
            print("Input 1: if Satisfied, 0: if Not") 
            print(passwordRandomizer(FirstName,LastName,BirthMonth,BirthDate,BirthYear))

            #Checker
            while True:
                c2 = input("-->")
                try:
                    int(c2)
                    break
                except ValueError:
                    print("Input a Number")

            #Logic
            if int(c2) == 1:
                break   

            

    elif ic == 2:
        pass

    elif ic == 3:
        pass
        
