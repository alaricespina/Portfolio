#Reverse Cipher Method
message = "Simple Text"
print("Original Text: " + message)
translated = ""

n = len(message) - 1

while n >= 0:
	translated += message[n]
	n -= 1

print("Final Result is: " + translated)
