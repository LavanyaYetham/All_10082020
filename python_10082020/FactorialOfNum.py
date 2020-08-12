#!/usr/local/bin/python3.8
num=int(input("Please Enter the Number: "))
a=num
while num > 1:
    b=num-1
    a=a*b
    num=b
print (a)
