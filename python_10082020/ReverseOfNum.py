#!/usr/local/bin/python3.8

num=int(input("Please Enter the Number: "))
z=0
while int(num) > 0:
    r=int(num)%10
    q=int(num)/10
    z=r+(z*10)
    num=int(q)
print (z)
