'''
Tuple------------------
ordered and unchangeable. 
Allows duplicate members.

Written with round brackets (parenthesis).
'''

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[1]) # "apple"
print(thistuple[-1]) # "cherry"

#Same mechanics as list for accessing items

'''
To change the things inside a tuple
Tuple must be first converted to list
then changes will be applied to the list
and return back to tuple
since tuples are immutable or unchangeable

This rule applies to changing any element
except if u want to add two tuples
'''

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

print(x.index("apple")) #returns 0
print(x.count("banana")) #returns 1

#To Add two tuples together
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

