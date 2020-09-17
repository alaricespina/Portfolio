'''
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, 
but can only have one expression.
'''

#Example 1
x = lambda a : a + 10
print(x(5))

#Example 2
x = lambda a, b : a * b
print(x(5, 6))

#Example 3
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#power of lambda
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) #Returns 22
print(mytripler(11)) #Returns 33