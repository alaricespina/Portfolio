import random

while True:
    print("Guess what could be the random number: [0-10]")
    while True:
        try:
            a = input("Number:")
            int(a)
            break
        except ValueError:
            print("Input only a number")

    randomnumber = random.randint(0,10)
    aint = int(a)
    if randomnumber == aint:
        print(f"You guessed the number {randomnumber} correctly")
    else:
        print(f"You were wrong, {aint} was not the number")

    print("Try again?")
    retry = input("Yes or No")
    if retry.lower() == "no": 
        break
    elif retry.lower() == "yes": 
        print("Ok then") 
    else: 
        print("Wat?")