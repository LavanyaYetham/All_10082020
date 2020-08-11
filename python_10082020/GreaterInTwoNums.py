#!/usr/local/bin/python3.8
num1=int(input("Please enter the number1: "))
num2=int(input("Please enter the number2: "))
if num1 > num2:
     print (num1,"is greater than",num2)
elif num2 > num1:
    print (num2,"is greater than",num1)
else:
    print (num1,num2,"are equal number")
print ("**************")
#To find greatest of two numbers using the built-in function
print (max(num1,num2),"is Greater Number")
print ("**************")
#To find greatest of two numbers using an arithmetic operator
if (num1-num2 > 0):
    print (num1,"is greater number")
elif (num2-num1 > 0):
    print (num2,"is greater number")
else:
    print (num1,num2,"are equal numbers")
print ("**************")
#To find greatest of two numbers using Function
def func(a,b):
    if a > b :
        print (a,"is Greater than",b)
    elif b > a :
         print (b,"is greater than",a)
    else:
        print (a,b,"are equal Numbers")
func(num1,num2)
