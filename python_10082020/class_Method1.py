#!/usr/local/bin/python3.8
class Myclass:
    name="noname"
    number=0
    def Set(self,name,number):
        self.name=name
        self.number=number
obj=Myclass()
obj.Set("ABCD",3)
print (obj.name)
print (obj.number)
print ("********")
class Myclass():
    name="noname"
    number=0
    def Set(self,name,number):
        self.name=name
        self.number=number
def Main():
    obj=Myclass()
    obj.Set("ABCD",2)
    print (obj.name)
    print (obj.number)
Main()
