#!/usr/local/bin/python3.8
num1=int(input("Please enter the numberi1: "))
num2=int(input("Please enter the numberi2: "))
num3=int(input("Please enter the numberi3: "))
if num1 > num2 and num1 > num3:
    print (num1,"is Greater number")
elif num2 > num1 and num2 > num3:
    print (num2,"is greater number")
elif num3 > num1 and num3 > num2:
    print (num3,"is greater nummber")
else:
    print (num1,num2,num3,"are Equal Numbers")
print ("**********")
def func(a,b,c):
    if a > b and a > c:
        print (a,"is Greater number")
    elif b > a and b > c:
        print (b,"is greater number")
    elif c > a and c > b:
        print (c,"is greater nummber")
    else:
        print (a,b,c,"are Equal Numbers")
func(num1,num2,num3)
print ("**********")
def func(a,b,c):
    if a > b and a > c:
        Large=a
    elif b > a and b > c:
        Large=b
    elif c > a and c > b:
        Large=c
    else:
        Large=a,b,c,"are Equal Numbers"
    return Large
print(func(num1,num2,num3))
