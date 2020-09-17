'''
List------------------
ordered and changeable. 
Allows duplicate members.

Written with square brackets.
'''

thislist = ["apple", "banana", "cherry"]
print(thislist)

print(thislist[1]) #Print apple

print(thislist[-1]) #Print cherry

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #Print cherry,orange,kiwi, 5th one(melon) is not included

print(thislist[:4]) #Prints apple,banana,cherry,orange

print(thislist[2:]) #Prints cherry until end

print(thislist[-4:-1]) #print orange to melon
# -4 is included while -1 not included

#Loop through the list
for x in thislist:
	print(x) #Prints all everything from the list

#Check if in list
if "apple" in thelist:
	print("The fruit is in the List")

#list length
print(len(thelist)) #Prints 3

#Insert items

#Append
thislist = ["apple", "banana", "cherry"]
thislist.append("orange") #Orange at the end
print(thislist)

#Insert
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") #Orange at index 1
print(thislist)

#Remove Items

#Remove(value)
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") 
print(thislist)

#pop(index), if no index, end of list will be removed
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#del list[index]
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#deletes list completely
del thislist

#listvariable.clear()
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

########################################

'''
Copying a list

You cannot copy a list simply by typing 
list2 = list1, 
because: list2 will only be a reference to list1,

and changes made in list1 will automatically 
also be made in list2.
'''

#copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#list(original list) method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

########################################

'''
Joining Lists
'''

#Using Addition
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Using append and for loop
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#Using extend
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

'''
For Additional methods

https://www.w3schools.com/python/python_lists.asp

'''