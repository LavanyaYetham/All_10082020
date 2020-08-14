#!/usr/local/bin/python3.8
'''
The factorial of a number is the product of all the integers from 1 to that number
'''
num=int(input("Please Enter the Number: "))
a=num
while num > 1:
    b=num-1
    a=a*b
    num=b
print (a)

print ('++Anther Way+++')
def factorial(num):
    if num == 1:
        return num
    else:
        return num*factorial(num-1)
num=int(input("Please enter the Number:"))
if num < 0:
    print ("Factorial cannot be found for negative numbers")
elif num == 0:
    print ("Factorial od 0 is :",1)
else:
    print ("Factorial of",num,"is: ",factorial(num))
 
