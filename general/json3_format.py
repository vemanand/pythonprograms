'''
In json1.py and json2.py we saw that you can convert Python object to Json string using dumps() method
This method takes additional arguments that can be used to format the result properly
Use the indent parameter to define the numbers of indents
Define separators to separate each object and to separate keys & values within the object
Use the sort_keys parameter to specify if the result should be sorted or not
'''

import json

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

#json_str = json.dumps(x, indent=4)
json_str = json.dumps(x, indent=4, separators=(". ", " = "))
json_sort = json.dumps(x, indent=4, sort_keys=True)
print(json_str)
print("Printing JSON after sorting")
print(json_sort)