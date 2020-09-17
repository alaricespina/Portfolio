'''
Iterator
object that contains a countable number of values.

Lists, tuples, dictionaries, and sets 
are all iterable objects.

They are iterable containers 
which you can get an iterator from.
'''

#Tuple Iterator
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#String Iterator
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#For loop, Tuple Iterating
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
	print(x)

#For loop, String Iterating
mystr = "banana"

for x in mystr:
	print(x)

#creating a class for iteration, upto 20x
class MyNumbers:
	def __iter__(self):
		self.a = 1
		return self

	def __next__(self):
		if self.a <= 20:
			x = self.a
			self.a += 1
			return x
		else:
		  	raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
	print(x)

