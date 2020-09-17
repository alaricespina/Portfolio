#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
'''
2myvar = "John"
my-var = "John"
my var = "John"
'''

#Multiple assignments in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x) #Prints Orange
print(y) #Prints Banana
print(z) #Prints Cherry

#Multiple variables assigned to one value
x = y = z = "Orange"
print(x) 
print(y)
print(z)
#All of them pritns Orange

#---------------------------------
#Global Variables
#---------------------------------


x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Prints out "Python is awesome"


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
#Prints out Python is fantastic

print("Python is " + x)
#Prints out "Python is awesome"

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#Both myfunc and this print would say 
#"Python is fantastic"