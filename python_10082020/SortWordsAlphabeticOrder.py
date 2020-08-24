#!/usr/local/bin/python3.8
#Python Program to Sort Words in Alphabetic Order
String = input("Enter the string: ")
Words=String.split()
Words.sort()
print (Words)
print ("****************")
for word in Words:
    print (word)
