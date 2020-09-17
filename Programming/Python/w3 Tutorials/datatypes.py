x1 = "Hello World"	
x2 = 20		
x3 = 20.5		
x4 = 1j		
x5 = ["apple", "banana", "cherry"]		
x6 = ("apple", "banana", "cherry")		
x7 = range(6)		
x8 = {"name" : "John", "age" : 36}		
x9 = {"apple", "banana", "cherry"}		
x10 = frozenset({"apple", "banana", "cherry"})
x11 = True		
x12 = b"Hello"		
x13 = bytearray(5)		
x14 = memoryview(bytes(5))	

a = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14]

for x in a: print(x)
for y in a: print(type(x))

''' Types of the variables from x1 - x14
str	
int	
float	
complex	
list	
tuple	
range	
dict	
set	
frozenset	
bool	
bytes	
bytearray	
memoryview

'''