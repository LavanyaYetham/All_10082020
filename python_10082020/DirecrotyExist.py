#!/usr/local/bin/python3.8
import os
dirname=input("Please enter the File: ")
if os.path.isdir("fname"):
    print (dirname,"is Existed and It is a File")
else:
    print (dirname,"is Not Existed")
