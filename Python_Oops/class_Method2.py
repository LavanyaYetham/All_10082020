#!/usr/local/bin/python3.8
class Myclass:
    name="noname"
    number=0
    def __init__(self,name,number):
        self.name=name
        self.number=number
obj=Myclass("abcd",1)
print (obj.name)
print (obj.number)

print ("************")
class One():
    def __init__(self,name,number):
        self.name=name
        self.number=number
obj=One("ABCD",2)
print (obj.name)
print (obj.number)

print ("********")
class Two():
    def __init__(self,name,number):
        self.name=name
        self.number=number
    def func(self):
        print (self.name)
        print (self.number)
obj2=Two("XYZ",3)
obj2.func()
