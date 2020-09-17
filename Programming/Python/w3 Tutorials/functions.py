'''
function 

block of code which only runs when it is called.
You can pass data(parameters) into a function.
A function can return data as a result.
'''

#creating a function
def my_function():
  print("Hello from a function")

#calling that function
my_function()

#function with an argument
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#difference of parameter and argument

my_function("Hatdog") #Hatdog is the argument

'''
def my_function(fname): <--- fname is the parameter
	print(fname)

both are the same information passed
'''

#Multiple arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes") #2 arguments because of 2 parameters in function

#Arbitrary(optional) arguments
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#Prints Linus

#Keyword arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

#Linus will be youngest
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#different, Emil will be youngest
my_function("Emil","Tobias","Linus")

#Arbitrary(optional) Keyword arguments
#function will receive a dictionary
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Default parameter value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function() #Will print Norway, since no argument is given
my_function("Brazil")

#Passing a List as argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#pass statement
def myfunction():
  pass

#Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6) #Prints 1,3,6,10,15,21