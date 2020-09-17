correctdict = {
    "energy": ["capacity to do work", "hatdog"]
}

print("What is energy")
trial = input("Answer:")
if trial in correctdict["energy"]:
    print("Correct")
else:
    print("Wrong")

print(correctdict["energy"])