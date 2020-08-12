#!/usr/local/bin/python3.8
Year=int(input("Please enter the Year: "))
if Year%4 == 0:
    if Year%100 == 0:
        if Year%400 == 0:
            print (Year,"is Leap Year")
        else:
            print (Year,"is not Leap Year")
    else:
        print (Year,"is Leap Year")
else:
    print (Year,"is not Leap Year")
