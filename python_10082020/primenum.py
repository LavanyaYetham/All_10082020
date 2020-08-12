#!/usr/local/bin/python3.8
num=int(input("Please enter the number: "))
if num >=2:
    for i in range(2,num):
        if (num%i) == 0 :
            print (num,"is not a Prime number")
            break
    else:
        print (num,"is  a Prime Number")
else:
    print (num,"is not a Prime Number")
