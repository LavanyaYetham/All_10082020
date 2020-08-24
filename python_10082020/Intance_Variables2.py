#!/usr/local/bin/python3.8
class Text:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30
t1=Text() #a,b willbe added to the object
t1.m1()  #c willbe added to the object
t1.d=40  #d willbe added to the object
t2=Text
print (t1.__dict__)
print (t2.__dict__)


