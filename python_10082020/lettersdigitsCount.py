#!/usr/local/bin/python3.8
s = input("Please enter the input: ")
DIGITS=0
LETTERS=0
for c in s:
    if c.isdigit():
        DIGITS+=1
    elif c.isalpha():
        LETTERS+=1
    else:
        pass
print ("LETTERS", LETTERS)
print ("DIGITS", DIGITS)
