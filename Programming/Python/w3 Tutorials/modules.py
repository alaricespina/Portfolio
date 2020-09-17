import platform #Built-in Module
import mymodules #Created Module

mymodules.greeting("Jonathan")
a = mymodules.person1["age"]
print(a)

x = platform.system()
print(x)

#list down all function and variable names of the module
x = dir(platform)
print(x)

#Importing only person1 from mymodule
from mymodules import person1

print (person1["age"])