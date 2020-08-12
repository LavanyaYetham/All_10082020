#!/usr/local/bin/python3.8
a=int(input("Please enter the number: "))
for b in range(1,11):
    c=a*b
    print (a,"*",b,"=",c)

print ("*********")
def func(num):
    for b in range(1,11):
        c=num*b
        print (num,"*",b,"=",c)
func(a)
