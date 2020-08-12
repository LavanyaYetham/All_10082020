#!/usr/local/bin/python3.8
import os
fname=input("Please enter the File: ")
if os.path.isfile("fname"):
    print (fname,"is Existed and It is a File")
else:
    print (fname,"is Not Existed")
