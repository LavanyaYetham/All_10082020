#!/usr/local/bin/python3.8
'''
Armstrong number is a number that is equal to the sum of n-th(n - number of digits) powers of their digits are called Armstrong numbers.
'''
startn=int(input("Please enter the starting Range: "))
endn=int(input("Please enter the ending Range: "))
for num in range(startn,endn+1):
    New=num
    Len=len(str(num))
    z=0
    while int(num) > 0:
        r=int(num)%10
        q=int(num)/10
        x=(r**Len)
        z=z+x
        num=int(q)
    if int(z) == int(New):
        print (New)
