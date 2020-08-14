#!/usr/local/bin/python3.8
'''
Armstrong number is a number that is equal to the sum of n-th(n - number of digits) powers of their digits are called Armstrong numbers.
'''
num=int(input("Please enter the Number: "))
New=num
Len=len(str(num))
z=0
while int(num) > 0:
    r=int(num)%10
    q=int(num)/10
    x=(r**Len)
    z=z+x
    num=int(q)
if z == New:
    print ("The Given Number",New,"is Armstrong Number")
else:
    print ("The Given Number",New,"is  not Armstrong Number")

