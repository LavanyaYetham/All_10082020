#!/usr/local/bin/python3.8
num=int(input("Please enter the number: "))
if num%2 == 0:
    print (num,"is even number")
else:
    print (num,"is not even number")

print ("************************")

def even_fun(n):
    return n%2 == 0
nums=[1,2,3,4,5,6]
evens=list(filter(even_fun,nums))
print (evens)
