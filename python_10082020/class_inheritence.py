#!/usr/local/bin/python3.8
class parent:
    def __init__(self,name,number):
        self.name=name
        self.number=number
class child(parent):
    def __init__(self,name,number):
        super().__init__(name,number)
def Main():
    obj1=parent("ABCD",1)
    obj2=child("XYZ",2)
    print ("---parent details---")
    print (obj1.name)
    print (obj2.number)
    print ("---",obj2.name,"details---")
    print ("Name: ",str(obj2.name))
    print ("Number: ",str(obj2.number))
Main()
