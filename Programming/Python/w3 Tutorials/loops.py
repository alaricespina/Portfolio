#while loop
i = 1
while i < 6:
  print(i)
  i += 1

#break statement, will stop when i is equal to 3
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#continue statement, will proceed when i == 3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#else statement, run once after condition is no longer true
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

##########################################

#for loop

#for loop through a string
for x in "banana":
  print(x)

#break statement, will stop once it reaches condition
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#same as above but print is below break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#for loop with range() 
for x in range(6): #starts at 0 ends at 5
  print(x)

for x in range(2, 6): #starts at 2 ends at 5
  print(x)

for x in range(2, 30, 3): #starts at 2 ends at 29
  print(x)
  #the results will be 2,5,8,11,14,17,20,23,26,29

#else statement just like the one for while loops
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#nested for loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#pass statement
for x in [0, 1, 2]:
  pass