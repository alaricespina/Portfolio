#Decrypting COlumnar Transposition
#Transposition Cipher
import math, numpy
msg = "Hore llWdlo"
print(msg)
new = ""
divx = 4
divy = math.ceil(len(msg)/divx)
limit = math.ceil(((4/9)*len(msg))-(8/9))
n = 1
while n <= limit:
	new = ""
	for x in numpy.arange(0, divx,1):
		for y in numpy.arange(0, divy, 1):
			z = x + (divx*y)
			print(z)
			if z <= len(msg)-1:
				new += msg[z]

	msg = ""
	msg = new
	print(msg)
	n += 1

print(limit)



