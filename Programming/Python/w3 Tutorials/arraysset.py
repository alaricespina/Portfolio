'''
Set------------------
unordered and unindexed. 
No duplicate members.

Written with curly brackets.
'''

thisset = {"apple", "banana", "cherry"}
print(thisset)


#Accessing Items

''' 
since sets are unordered
there are no index
you can only use 

for x in thisset or
if x in thisset 

to know if a value exist
'''
for x in thisset:
  print(x)

print("banana" in thisset) #True

#Adding items

#add(item) method
thisset = {"apple", "banana", "cherry"}
thisset.add("orange") #will add at the start of set
print(thisset)

#update(set) method

thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

#Length of the set
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) #3

#Removing items

#remove(item) method
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#discard(item) method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#pop() method, cant put index number since set is unordered
thisset = {"apple", "banana", "cherry"}
x = thisset.pop() #the last item only
print(x)
print(thisset)

#clear() method
thisset = {"apple", "banana", "cherry"}
thisset.clear() #removes all
print(thisset)

#del item method
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

#Join Two Sets

#union(other set) method
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#update(other set) method
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#both union and update will remove duplicates

'''
For more methods

https://www.w3schools.com/python/python_sets.asp
'''