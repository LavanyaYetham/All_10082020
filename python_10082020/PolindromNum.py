#!/usr/local/bin/python3.8
num=int(input("Please enter the Number: "))
New=num
z=0
while int(num) > 0:
    r=int(num)%10
    q=int(num)/10
    z=r+(z*10)
    num=int(q)
if int(z) == int(New):
   print ("The Given Number",New,"is Polindrome")
else:
   print ("The Given Number",New,"is not  Polindrome")

