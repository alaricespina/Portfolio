class Employee:
	def __init__(self, name):
		self.name = name

	def empAge(self,empAge):
		self.age = empAge

	def empDesignation(self,empDesig):
		self.designation = empDesig

	def empSalary(self,empSalary):
		self.salary = empSalary

	def printEmployee(self):
		print(f"Name: {self.name}")
		print(f"Age: {self.age}")
		print(f"Designation: {self.designation}")
		print(f"Salary: {self.salary}")

