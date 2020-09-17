'''
Dictionary------------------ 
unordered, changeable and indexed. 
No duplicate members.

Written with curly brackets, 
with its keys and values.
'''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

x = thisdict["model"]
y = thisdict.get("model")

#Both will be equal to "Mustang"

#Changing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#For looping

#Prints out the keys only (brand,model,year)
for x in thisdict:
  print(x)

#Prints out the values only (Ford,Mustang,1964)
for x in thisdict:
  print(thisdict[x])

for x in thisdict.values():
  print(x)

#Both Keys and values
for x, y in thisdict.items():
  print(x, y)

#Checking
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#Check if key exist
if "model" in thisdict:
	print("Yes")

#Check if value exists
if "Mustang" in thisdict.values():
	print("Yes")

#Dictionary Length
print(len(thisdict)) #Returns 3

#Adding items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#Removing items

#pop(key) method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#popitem() method, removes last inserted item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964 #This will be deleted
}
thisdict.popitem()
print(thisdict)

#del method
thisdict = {
  "brand": "Ford",
  "model": "Mustang", #Will be removed
  "year": 1964
}
del thisdict["model"]
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict #Remove the dictionary completely

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear() #Clears the dictionary
print(thisdict)

###########################################
'''
Copying a dictionary

You cannot copy a dictionary simply by typing 
dict2 = dict1, 
because: dict2 will only be a reference to dict1, 
and changes made in dict1 will automatically 
also be made in dict2.
'''

#copy() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#dict() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child1"]["name"]) #prints Emil

#Same as above
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"]) #prints Tobias