UsLi = []
PaLi = []
DiSi = []
import time
print ("Hello! This is PHubCommunity!");
time.sleep(1.0)

intro = input("Do you have a PHubCommunity account? Please type Yes or No:")
if intro == "No":
    print("Then Please Register Below")
    time.sleep(1.0)
    print("Honesty is the best Policy :)")
    UsNa = input("Please type your desired username: ")
    UsLi.append(UsNa)
    time.sleep(1.0)
    Pass = input ("And please type your desired password: ")
    PaLi.append(Pass)
    time.sleep(1.0)
    print("(If you don't have, just type 0)")
    n = 1
    while n:
        Dick = input("Now please type in your Dick size (Inches): ")
        try:
            DiSi.append(int(Dick))
            n = 0
        except ValueError:
            print("Invalid Size")
    time.sleep(1.0)
    print("Thank You for being a new Member!")
    time.sleep(1.0)
    print("Now, Please Login with your New Account")
    time.sleep(1.0)
    Usname1 = input("Username: ")
    Passwo1 = input("Password: ")
    n = 1
    while n:
        Dicksi1 = input("Dick Size: ")
        try:
            a = int(Dicksi1)
            n = 0
        except ValueError:
            print("Invalid Size")
   
    if Usname1 in UsLi and Passwo1 in PaLi and int(Dicksi1) in DiSi:
        print("Welcome to the PHUB Community fellow Member!")
    else:
        print("Incorrect Username, Password, or Dick Size")


if intro == "Yes":
    print("Please Login your existing account")
    Usname2 = input("Type in your Username:")
    Passwo2 = input("Type in your password:")
    Dicksi2 = input("Type in your dicksize:")
    if Usname2 in UsLi and Passwo2 in PaLi and Dicksi2 in DiSi:
        print("Welcome to the PHUB Community fellow Member!")
    else:
        print("Incorrect Username, Password, or Dick Size")