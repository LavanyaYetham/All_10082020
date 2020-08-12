#!/usr/local/bin/python3.8
startn=int(input("please enter the starting range: "))
endn=int(input("please enter the ending range: "))
for num in range(startn,endn+1):
    New=num
    z=0
    while int(num) > 0:
        r=int(num)%10
        q=int(num)/10
        z=r+(z*10)
        num=int(q)
    if z == New:
        print (New)
