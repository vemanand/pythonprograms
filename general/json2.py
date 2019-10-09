'''
Python has a built-in package called json, which can be used to work with JSON data.
you can parse JSON string by using the json.loads(<string>) method. This returns a Python dictionary
you can convert Python object into a JSON string by using the json.dumps(<object>) method. This returns a Json string
The qualified objects are list, dict, tuple, string, int, float, bool
This program converts Json string to Python Object and also an object to Json string
'''
import json

print("Converting several Python objects to Json using dumps method")
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print("Converting Python object having all legal types to Json string")
obj = {
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

print(json.dumps(obj))