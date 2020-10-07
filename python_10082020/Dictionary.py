#!/usr/local/bin/python3.6

d1={"name":"Abcd","num":123,"location":"xyz"}
print (d1)
print (d1['name'])
print (d1.get('name'))
print ('#################')
for i in d1:
    print (i)
print ('#################')
for j in d1.keys():
    print (j)
print ('#################')
for k in d1.values():
    print (k)
print ('#################')
for a,b in d1.items():
    print (a,":",b)
print ('#################')
#change the dicttionary value
d1['num']=456
print (d1)
print ('#################')
print ('Length of dictionary is: ',end="")
print (len(d1))
print ('#################')
#Adding  items to Dictionary
d1['colour']="White"
print (d1)
print ('#################')
#Removing the items from Dictionary
d1.pop('name')
print (d1)
#popitem() remove the last item from the Dictionary
d1.popitem()
print (d1)
print ('#################')
#The del keyword removes the item with the specified key name
del d1['num']
print (d1)
print ('#################')
#The clear() method empties the dictionary
d1.clear()
print (d1)
d2={'name':"XYZ","num":321,"Location":"abcd"}
print ('#################')
#copying the Dictionary
#1)copy()
d3=d2.copy()
print (d3)
print ('#################')
#dict()
d4=dict(d2)
print (d4)
print ('#################')
#dict() Constructor:- It is also possible to use the dict() constructor to make a new dictionary
d5=dict(name="tgb",num=345,Location="edc")
print (d5)
