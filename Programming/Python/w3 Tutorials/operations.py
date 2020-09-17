a = 10
b = 20
'''
-----------------------------
Arithmetic Operators
-----------------------------
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus (Remainder)	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
'''
print("-----------")
print(a+b)
print(a-b)
print(a*b)
print(b/a)

c = 3
d = 2
print("-----------")
print(c%d) #returns 1
print(c**d) #returns 9
print(c//d) #returns 1


##########################################

'''
-----------------------------
Assignment Operators
-----------------------------
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3 <-- BITWISE OPERATOR	
|=	x |= 3	x = x | 3 <-- BITWISE OPERATOR	
^=	x ^= 3	x = x ^ 3 <-- BITWISE OPERATOR
>>=	x >>= 3	x = x >> 3 <-- BITWISE OPERATOR	
<<=	x <<= 3	x = x << 3 <-- BITWISE OPERATOR
'''
e = 10
f = 20

e += f # e = e + f or e = 10 + 20 which is 30
e -= f # e = e - f or e = 30 - 20 which is 10
e *= f # e = e * f or e = 10 * 20 which is 200
e /= f # e = e / f or e = 200 / 20 which is 10
e %= f # e = e % f or e = 10 % 20 which is 10 (remainder)
e //= f # e = e // f or e = 10 // 20 which is 0 (whole before remainder)
e **= f # e = e ** f or e = 0 ** 20 which is 0


##########################################

'''
-----------------------------
Comparison Operators
-----------------------------

==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y	

'''

g = 100
h = 200
print("-----------")
if g == h: print("1") #False
if g != h: print("2") #True
if g > h: print("3") #False
if g < h: print("4") #True
if g >= h: print("5") #False
if g <= h: print("6") #True
print("-----------")


##########################################

'''
-----------------------------
Logical Operators
-----------------------------

and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

'''

i = 69
j = 123

if i < j and j > i: print(True)
if i < j or j < i: print(True)
if not (i < j and j > i): print(True) #Will not print


##########################################

'''
-----------------------------
Identity and Membership Operators
-----------------------------

Identity:

is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y

Membership:

in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y

'''

#Identity
class Hallo:
	def __init___(self):
		self.state = True

hatdog = Hallo()
lmao = Hallo()
roflmao = hatdog

print("-----------")
if hatdog is lmao: print("Yes")
if hatdog is not lmao: print("Not same")
if hatdog is roflmao: print("Yeah it is")
print("-----------")

#Membership
k = [1,2,3,4,5]
l = 3

if l in k : print("In")
if l not in k: print("Out")
print("-----------")