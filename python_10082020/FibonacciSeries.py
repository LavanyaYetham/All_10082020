#!/usr/local/bin/python3.8
'''
a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
'''
num=int(input("Please enter the Number: "))
a=0
b=1
c=a+b
while c <= num:
    print (c) 
    a=b
    b=c
    c=a+b
print ("****Another Way using Function***")
def recur_fibo(n):
    if n <= 1:
        return 1
    else:
        return (recur_fibo(n-1)+recur_fibo(n-2))
number=int(input("Please enter the number: "))
if number <= 0:
    print ("Please enter the Positive Ineger")
else:
    print ("Fibonacci Series: ")
    for i in range(number):
        print (recur_fibo(i))



