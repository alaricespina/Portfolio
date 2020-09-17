#Coding Challenge 1

import random

def memify(text):
    atext = []
    for x in text:
        choice = random.randint(0,1)
        if choice:
            atext.append(x.upper())
        else:
            atext.append(x.lower())
    
    return "".join(atext)

print("CODING CHALLENGE:\n")
print(memify("Random Capitalization for every letter\n"))
print(memify("Hint: Use random module"))
print(memify("Hint #2: Convert the string to an array\n"))

print("\nExample Results from the function:\n")
print(memify("\nLorem ipsum dolor sit amet, consectetur adipiscing elit.\n Phasellus eros metus, suscipit in arcu eu, convallis gravida felis.\n Quisque rhoncus porttitor ex vel tristique. Sed at pellentesque ex.\n Nulla hendrerit odio a lorem rutrum porta. Quisque mauris magna, ornare\n at consequat ut, sollicitudin in enim. Vestibulum ullamcorper\n lobortis dui, at vestibulum felis. Maecenas consequat\n massa at diam molestie dictum. Integer euismod pharetra orci, quis\n"))