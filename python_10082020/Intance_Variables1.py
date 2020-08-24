#!/usr/local/bin/python3.8
class Text:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30
t=Text() #a,b willbe added to the object
t.m1()  #c willbe added to the object
t.d=40  #d willbe added to the object

print (t.__dict__)
