#Transposition Cipher
import math, numpy
msg = "Hello World"
print(msg)
new = ""
divx = 4
divy = math.ceil(len(msg)/divx)

for x in numpy.arange(0, divx,1):
	for y in numpy.arange(0, divy, 1):
		z = x + (divx*y)
		print(z)
		if z <= len(msg)-1:
			new += msg[z]
print(new)




