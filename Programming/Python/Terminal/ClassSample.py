import random

class RandomThing:
    def __init__(self, name):
        self.newValue()
        self.name = name

    def newValue(self):
        self.number = random.randint(0,10)

    def displayValue(self):
        print(f"{self.name}'s Current Value: {self.number}")
    
first = RandomThing("first")
second = RandomThing("second")
third = RandomThing("third")

first.displayValue()
second.displayValue()
third.displayValue()

while True:
    values = [first,second,third]
    print("\nInput either [display], [new value], or [quit] to stop")
    a = input("\nAction:")
    if a.lower() == "display":
        for x in values: x.displayValue()
    if a.lower() == "new value":
        print("\nNew Value Generated")
        for x in values: 
            x.newValue()
            x.displayValue()
    if a.lower() == "quit":
        print("\nGood Day Sir!")
        break
