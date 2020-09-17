a = "Hello"
print(a)

#Multi line strings can also use '''
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Strings as arrays
a = "Hello, World!"
print(a[1]) #prints e

#Slicing Strings
b = "Hello, World!"
print(b[2:5]) #prints llo

#Negative Index Slicing | Starts at the end 
b = "Hello, World!"
print(b[-5:-2]) #prints orl
print(b[-2:-5]) #Does not print anything

#String Length
a = "Hello, World!"
print(len(a)) #prints 13

#------------------------------------------------
#--------------String Methods--------------------
#------------------------------------------------

#Strip
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Lower
a = "Hello, World!"
print(a.lower()) # returns hello, world!

#Upper
a = "Hello, World!"
print(a.upper()) # returns HELLO, WORLD!

#Replace
a = "Hello, World!"
print(a.replace("H", "J")) # returns Jello, World!

#Split
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#---------------------------------

#Check String in the string
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x) #returns True

#String Concatenation (Adding Two Strings)
a = "Hello"
b = "World"
c = a + b
print(c) #returns HelloWorld

#format method, same as print(f"") method
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#The Numbers are to specify which of the
#formatted variables is to be used on that
#part, quantity is 0, itemno is 1, price is 2

#printf version of the thing above
print(f"I want to pay {price} dollars for {quantity} pieces of item {itemno}")
