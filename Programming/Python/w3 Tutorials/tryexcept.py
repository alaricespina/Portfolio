try:
	print(x)
except:
	print("An exception occurred")

#error because x is not yet defined

#1 Try can have multiple exceptions
try:
	print(x)
except NameError:
	print("Variable x is not defined")
except:
	print("Something else went wrong")

#Else to be executed when there is no error
try:
	print("Hello")
except:
	print("Something went wrong")
else:
	print("Nothing went wrong")

#finally will be exectued regardless of error
try:
	print(x)
except:
	print("Something went wrong")
finally:
	print("The 'try except' is finished")  

#Raising an Exception
x = -1

if x < 0:
	raise Exception("Sorry, no numbers below zero")

#TypeError
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

