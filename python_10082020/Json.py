#!/usr/local/bin/python3.6
import json
x='{ "name":"John", "age":30, "city":"New York"}'
print (x)
print (type(x))
y=json.loads(x)
print (y)
print (type(y))

a= {
  "name": "John",
  "age": 30,
  "city": "New York"
}
print (a)
print (type(a))

b=json.dumps(a)
print (b)
print (type(b))

c= {
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
print (c)
print (type(c))

d=json.dumps(c,indent=4)
print (d)
print ("******************")
e=json.dumps(c,indent=4,sort_keys=True)
print (e)
