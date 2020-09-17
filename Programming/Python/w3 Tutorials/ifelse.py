'''
Python Conditions and If statements

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
'''

#if
a = 33
b = 200
if b > a:
  print("b is greater than a")

#elif , else if
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#else, anything not within previous conditions
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#you can also remove elif, its the same concept

#Short Hand If
if a > b: print("a is greater than b")

#Short Hand if else
a = 2
b = 330
print("A") if a > b else print("B")

#Multiple Short Hands
#Result if true, if condition, result if false (can be replaced to repeat)
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#Previous short hand can be expanded to this
a = 330
b = 330
if a > b:
	print("A")
elif a == b:
	print("=")
else:
	print("B")

#And Condition
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#Or Condition
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#Nested if else
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#pass statement (WIP types of projects)
#needed if theres an if but no content inside
a = 33
b = 200

if b > a:
  pass