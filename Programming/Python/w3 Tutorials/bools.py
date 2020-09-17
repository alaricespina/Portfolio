print(10 > 9)
print(10 == 9)
print(10 < 9)

print(bool("Hello"))
print(bool(15))

'''
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
'''

#False Values if converted to Bool
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#Functions can work as conditions
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#Another example of the use of bool
x = 200
print(isinstance(x, int))