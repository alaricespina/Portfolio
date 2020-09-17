'''
JSON 

syntax for storing and exchanging data.
text, written with JavaScript object notation.
'''
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"]) 

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#things that can be converted to JSON
print(json.dumps({"name": "John", "age": 30})) #dict
print(json.dumps(["apple", "bananas"])) #list
print(json.dumps(("apple", "bananas"))) #tuple
print(json.dumps("hello")) #string
print(json.dumps(42)) #int
print(json.dumps(31.76)) #float
print(json.dumps(True)) #bool
print(json.dumps(False)) #bool
print(json.dumps(None)) #NoneType

#######################################

#Formatting a JSON result

#Create a python object
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

#With Indent, and keys are sorted
print(json.dumps(x, indent=4, sort_keys=True))