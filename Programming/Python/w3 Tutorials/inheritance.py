'''
Inheritance 

define a class that inherits all the methods 
and properties from another class.

Parent class 
the class being inherited from, 
also called base class.

Child class 
the class that inherits from another class, 
also called derived class.
'''

#Parent Class
class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def printname(self):
		print(self.firstname + " " + self.lastname)		

x = Person("John", "Doe")
x.printname()

#Child Class
class Student(Person):
	def __init__(self, fname, lname, year):
		super().__init__(fname, lname) #super(), used to inherit all methods of parent
		self.graduationyear = year

	def welcome(self):
		print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

y = Student("Lala","Urara", 2020)
y.printname()
y.welcome()

#if you add another method to the child with the same name as the parent, the parent method will be overridden




