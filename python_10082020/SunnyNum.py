#!/usr/local/bin/python3.8
"""
A number n is said to be sunny number if square. root of(n+1) is an integer. e.g. 8 is a sunny number because sq.root of (8+1. )is 3 ,which is an integer.
"""
import math
num=int(input("Enter the Number: "))
x=math.sqrt(num+1)
print (x)
print (int(x))
print ("****")
if int(x) == x:
    print (num,"is Sunny Number")
else:
    print (num,"is not Sunny Number")
