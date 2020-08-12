#!/usr/local/bin/python3.8
s = input("Please enter the input: ")
UPPERCASE=0
LOWERCASE=0
for c in s:
    if c.isupper():
        UPPERCASE +=1
    elif c.islower():
        LOWERCASE +=1
    else:
        pass
print ("UPPER CASE", UPPERCASE)
print ("LOWER CASE", LOWERCASE)
