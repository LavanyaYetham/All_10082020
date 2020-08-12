#!/usr/local/bin/python3.8
num=int(input("Please enter the number: "))
value=1
print ("Factors of a given number",num,"are")
while value <=num:
    if (num % value == 0):
        print(value)
    value=value+1
print ("*********")
print ("Factors of a given number",num,"are")
for value in range(1,num+1):
    if (num % value == 0):
        print(value)
    value=value+1
