'''
File Handling

open(filename, modes)

modes

"r" - Read - 
Default value. Opens a file for reading, 
error if the file does not exist

"a" - Append - Opens a file for appending, 
creates the file if it does not exist

"w" - Write - Opens a file for writing, 
creates the file if it does not exist

"x" - Create - Creates the specified file, 
returns an error if the file exists

handle modes

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

must reopen txt file as each operations -
from the read file
'''

import os

#1
f = open("demofile.txt", "rt")

#2 same as #1
f = open("demofile.txt")

########################################
#Reading the file
f = open("demofile.txt", "r")
print(f.read())

#Reading only upto x characters
f = open("demofile.txt", "r")
print(f.read(5))

#Only the first line
f = open("demofile.txt", "r")
print(f.readline())

#Only the first to second line
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

#For Looping
print("------------")
f = open("demofile.txt", "r")
for x in f:
	print(x)

#Closing files, in order to save changes
f.close()

########################################

#Append
print("------------")
f = open("demofile2.txt", "a")
f.write("\nNow the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())


#Write (Overwrite)
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())

#Create a new file
if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
  print("File Removed")


f = open("myfile.txt", "x")

f = open("myfile.txt", "w")
f.write("\nThis sht exists now")

f = open("myfile.txt", "r")
print(f.read())
f.close()

os.remove("myfile.txt")
#Deleting a file