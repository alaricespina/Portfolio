'''
A Class is like an object constructor, 
or a "blueprint" for creating objects.
'''

#creating a class
class MyClass:
	x = 5

p1 = MyClass()
print(p1.x) #Prints 5

#More useful way of classes
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def myfunc(self):
		print("My Name is " + self.name)

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.myfunc()

#You can also opt not to use self
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#modify object properties
p1.age = 40

#delete object properties
del p1.age

#delete object
del p1

#self explanatory
class unfinishedClass:
	pass
