'''
Python has a built-in package called json, which can be used to work with JSON data.
you can parse JSON string by using the json.loads(<string>) method. This returns a Python dictionary
you can convert Python object into a JSON string by using the json.dumps(<object>) method. This returns a Json string
The qualified objects are list, dict, tuple, string, int, float, bool
This program converts Json string to Python Object and also an object to Json string
'''

import json

# Declar some JSON String
person =  '{ "name":"Ganesh", "age":30, "city":"Hyderabad"}'

# Parse the Json string using loads() method and display
print("Converting JSON string to object using loads method")
y = json.loads(person)
# the result is a Python dictionary:
print(y)
print(y["age"])

# Declar a Python object (dict)
pyobj = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# Convert Python object to JSON string using dumps() method and display
print("Converting Python object to Json string using dumps method")
y = json.dumps(pyobj)
print(y)