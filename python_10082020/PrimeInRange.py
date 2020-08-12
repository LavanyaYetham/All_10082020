#!/usr/local/bin/python3.8
startn=int(input("Please enter the starting range: "))
endn=int(input("Please enter the ending range: "))
for i in range(startn,endn+1):
    if i > 1:
        for j in range(2,i):
            if (i%j) == 0:
                break
        else:
            print (i)
